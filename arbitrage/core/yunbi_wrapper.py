from context import yunbi
import conf
import os
from copy import copy

interested_list = ["cny", "btc","sc"]
market = 'sccny'

class yunbi_wrapper():
	def __init__(self):
		dirpath=os.path.dirname(os.path.abspath(__file__))
		conf.init(dirpath + "/../account.ini")
		apikey = str(conf.get_value("yunbi", "apikey"))
		secret = str(conf.get_value("yunbi", "secret"))
		self.client = yunbi(apikey, secret)

	# "accounts":[{"currency":"cny","balance":"0.0","locked":"0.0"},{}]
	def balance(self):
		info = self.client.get('members')
		result = {}
		for item in info["accounts"]:
			for interested_key in interested_list:
				if item["currency"] == interested_key:
					result[interested_key] = item
					break

		return result

	def order_book(self):
		info = self.client.get('order_book', params={'market': market,'asks_limit': 50, 'bids_limit':50})
		asks = []
		for ask_item in info["asks"]:
			order_ask = order(ask_item)
			asks.append(order_ask)
		bids = []
		for bid_item in info['bids']:
			order_bid = order(bid_item)
			bids.append(bid_item)

		return asks, bids


class order():
	def __init__(self, source):
		self.created_at = ''
		self.trades_count = 0
		self.remaining_volume = 0
		self.price = 0
		self.side = 'buy'
		self.volume = 0
		self.state = 'wait'
		self.ord_type = 'limit'
		self.avg_price = 0
		self.executed_volume = 0
		self.id = 0
		self.market = 'sccny'

		self.update(**dict((k, self.parse(v))
                           for k, v in source.iteritems()))

		exit()

		print(dir(source))
		print(dir(self))

		# self.__dict__ = source.__dict__.copy()
		# self._parse(source)

	# def _parse(self, source):
	# 	self.__dict__.update(source.__dict__)
	# 	return self

if __name__ == '__main__':
	# t1 = {"a":0}

	# t2 = {"a":1,"b":2}

	# print(t2.iteritems())

	# exit()

	wrapper = yunbi_wrapper()
	print(wrapper.order_book())
