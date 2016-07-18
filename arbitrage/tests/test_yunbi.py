import os
import requests
from context import yunbi
from context import conf
from context import core

import unittest

class BasicTestSuite(unittest.TestCase):
	def setUp(self):
		dirpath=os.path.dirname(os.path.abspath(__file__))
		conf.init(dirpath + "/../account.ini")
		apikey = str(conf.get_value("yunbi", "apikey"))
		secret = str(conf.get_value("yunbi", "secret"))
		self.client = yunbi(apikey, secret)

	def test_get_markets(self):
		markets = self.client.get('markets')
		print(markets)

	def test_get_members(self):
		info = self.client.get('members')
		print(info)

	# def test_get_ticker(self):
	# 	path = self.client.get_api_path('tickers') % "sccny"
	# 	info = self.client.get_by_path(path)
	# 	print(info)

	# Get the order book of specified market
	def test_get_order_book(self):
		info = self.client.get('order_book', params={'market': 'sccny','asks_limit': 50, 'bids_limit':50})
		print(info)

	# Get your orders, results is paginated 
	def test_get_my_orders(self):
		info = self.client.get('orders', {'market': "sccny"})
		print(info)

	def test_get_my_trades(self):
		print self.client.get('my_trades', {'market': "sccny"})

	def test_post_clear(self):
		print self.client.post('clear')

	def test_post_orders(self):
		params = {'market': 'sccny', 'side': 'sell', 'volume': 10, 'price': 0.001}
		res = self.client.post('orders', params)
		print(res)

def test():
	dirpath=os.path.dirname(os.path.abspath(__file__))
	conf.init(dirpath + "/../account.ini")
	apikey = str(conf.get_value("yunbi", "apikey"))
	secret = str(conf.get_value("yunbi", "secret"))
	client = yunbi(apikey, secret)
	# params = {'market': 'sccny', 'side': 'sell', 'volume': 10, 'price': 0.001}
	# res = client.post('orders', params)

	print client.post('clear',None, False)

	# res = client.get('markets')

if __name__ == '__main__':
    # unittest.main()
    test()
    
