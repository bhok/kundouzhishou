# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
import core.conf as conf
import core.core as core

import json

import core.poloniex_wrapper as poloniex_wrapper

markets=['etc','fct','sc','lbc','amp']
point = 0.05
dirpath=os.path.dirname(os.path.abspath(__file__))
file_path = dirpath + '/info.json'
price_offset=[0.1,0.2,0.3,0.5]

push_over_id='au9kagozrxrp6xsrpit3cepymxhgkp'
ORDER_DEPTH = 5000

class exchange_monitor():
	def __init__(self):
		self.exchange = poloniex_wrapper(None,None)

	def ticker(self):
		new_info = self.exchange.ticker_pairs(markets)
		old_info = ''
		with open(file_path, 'rb') as f:
			old_info = json.loads(f.read())

			if len(old_info) == 0:
				old_info = new_info

		save_info = self._check(new_info, old_info)


		with open(file_path, 'wb') as f:
			f.write(json.dumps(save_info))

	def _check(self, new_info, old_info, is_test=False):
		for new_pair in new_info:
			for old_pair in old_info:
				if new_pair['currency'] == old_pair['currency']:
					offset = new_pair['price'] - old_pair['price']
					if offset / old_pair['price'] > point or offset / old_pair['price'] < -point:
						currency = new_pair['currency']

						if not is_test:
							bids, asks = self.exchange.order_book(currency, ORDER_DEPTH)
							self._record(currency, new_pair['price'], old_pair['price'], bids, asks)

						# change price
						old_pair['price'] = new_pair['price']

					break

		return old_info

	def _record(self, currency, new_price, old_price, bids, asks):
		rate = round((new_price - old_price) / old_price, 3) * 100

		print(currency)
		# print('bids = ',bids)
		# print('asks = ',asks)
		
		bid_volume_offset = {}
		for bid_order in bids:
			for p_offset in price_offset:
				if bid_order['price'] > new_price * (1 - p_offset):
					if p_offset in bid_volume_offset:
						bid_volume_offset[p_offset] += bid_order['volume'] * bid_order['price']
					else:
						bid_volume_offset[p_offset] = bid_order['volume'] * bid_order['price']

		ask_volume_offset = {}
		for ask_order in asks:
			for p_offset in price_offset:
				if ask_order['price'] < new_price * (1 + p_offset):
					if p_offset in ask_volume_offset:
						ask_volume_offset[p_offset] += ask_order['volume'] * ask_order['price']
					else:
						ask_volume_offset[p_offset] = ask_order['volume'] * ask_order['price']

		# deal with edge condition
		for p_offset in price_offset:
			if bids[-1]['price'] > new_price * (1 - p_offset):
				bid_volume_offset[p_offset] = 0
			if asks[-1]['price'] < new_price * (1 + p_offset):
				ask_volume_offset[p_offset] = 0

		for k,v in bid_volume_offset.iteritems():
			bid_volume_offset[k] = round(v,2)

		for k,v in ask_volume_offset.iteritems():
			ask_volume_offset[k] = round(v,2)

		msg = str.format('\nname={0},last_price={1},new_pair={2},offset={3}', currency, old_price, new_price, rate) + '\n'
		msg += str.format('bid volume = {0}\n', bid_volume_offset)
		msg += str.format('ask volume = {0}\n', ask_volume_offset)
		
		core.info(msg)
		core.pushover(push_over_id, msg)
		self._writeDB(currency, old_price, new_price, rate, bid_volume_offset, ask_volume_offset)

	def _writeDB(self, name,last_price,new_price,offset,bids_volumes, asks_volumes):
		inc_decs = []
		for i in price_offset:
			inc_decs.append(asks_volumes[i])
			inc_decs.append(bids_volumes[i])
		id_str = ','.join([str(x) for x in inc_decs])

		sql = str.format("insert into price_monitor(`name`,`last_price`,`new_price`,`offset`,\
			`volume_inc_10`, `volume_dec_10`,`volume_inc_20`, `volume_dec_20`,`volume_inc_30`,`volume_dec_30`,`volume_inc_50`,`volume_dec_50`)\
			 values('{0}',{1},{2},{3},{4})", name,last_price,new_price,offset, id_str)

		core.execute_sql(sql)

def ticker():
	exchange = exchange_monitor()
	exchange.ticker()

if __name__ == "__main__":
	ticker()
