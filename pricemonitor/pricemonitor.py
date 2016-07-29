# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
import core.conf as conf
import core.core as core

import json

import core.poloniex_wrapper as poloniex_wrapper

markets=['etc','fct','sc','lbc','amp']
point = 0.1
dirpath=os.path.dirname(os.path.abspath(__file__))
file_path = dirpath + '/info.json'
price_offset=[0.1,0.2,0.3,0.5]

class exchange_monitor():
	def __init__(self):
		self.exchange = poloniex_wrapper(None,None)

	def ticker(self):
		new_info = self.exchange.ticker_pairs(markets)
		old_info = ''
		with open(file_path, 'rb') as f:
			if len(old_info) == 0:
				old_info = new_info
			else:
				old_info = json.loads(f.read())

		self._check(new_info, old_info)


		with open(file_path, 'wb') as f:
			f.write(json.dumps(new_info))

		print(new_info)

	def _check(self, new_info, old_info):
		for new_pair in new_info:
			for old_pair in old_info:
				if new_pair['currency'] == old_pair['currency']:
					offset = new_pair['price'] - old_pair['price']
					if offset / old_pair['price'] > point or offset / old_pair['price'] < -point:
						currency = new_pair['currency']
						bids, asks = self.exchange.order_book(currency, 150)
						self._record(currency, new_pair['price'], old_pair['price'], bids, asks)

					break

	def _record(self, currency, new_price, old_price, bids, asks):
		rate = round((new_price - old_price) / old_price, 3) * 100

		print('bids = ',bids)
		print('asks = ',asks)
		
		bid_volume_offset = {}
		for bid_order in bids:
			for p_offset in price_offset:
				if bid_order['price'] > new_price * (1 - p_offset):
					if p_offset in bid_volume_offset:
						bid_volume_offset[p_offset] += float(bid_order['volume']) * float(bid_order['price'])
					else:
						bid_volume_offset[p_offset] = float(bid_order['volume']) * float(bid_order['price'])

					break

		ask_volume_offset = {}
		for ask_order in asks:
			for p_offset in price_offset:
				if ask_order['price'] < new_price * (1 + p_offset):
					if p_offset in ask_volume_offset:
						ask_volume_offset[p_offset] += ask_order['volume'] * ask_order['price']
					else:
						ask_volume_offset[p_offset] = ask_order['volume'] * ask_order['price']

					break

		for k,v in bid_volume_offset.iteritems():
			bid_volume_offset[k] = round(v,2)


		for k,v in ask_volume_offset.iteritems():
			ask_volume_offset[k] = round(v,2)

		print(str.format('name={0},last_price={1},new_pair={2},offset={3}', currency, old_price, new_price, rate))
		print('bid volume = ', bid_volume_offset)
		print('ask volume = ', ask_volume_offset)
		


def ticker():
	exchange = exchange_monitor()
	exchange.ticker()

if __name__ == "__main__":
	ticker()
