import os
import requests
from context import conf
from context import core
from context import exchange_pair

import unittest

class BasicTestSuite(unittest.TestCase):
	def setUp(self):
		self.exchange_pair = exchange_pair(None,None,None)
		self.exchange_pair._btc_cny_rate = 10

	def test_check(self):
		bids = [{'price':103,'volume':1000,'currency':'sc'},{'price':102,'volume':800,'currency':'sc'},{'price':101.5,'volume':1000,'currency':'sc'},{'price':99,'volume':1000,'currency':'sc'}]
		asks = [{'price':10.2,'volume':400,'currency':'btc'},{'price':10.25,'volume':200,'currency':'btc'},{'price':10.31,'volume':1000,'currency':'btc'},{'price':10.4,'volume':400,'currency':'btc'}]
		print(self.exchange_pair._check_bid_ask(bids, asks))

		bids = [{'price':103,'volume':1000,'currency':'sc'}]
		asks = [{'price':6.2,'volume':400,'currency':'btc'}]
		print(self.exchange_pair._check_bid_ask(bids, asks))

		bids = [{'price':103,'volume':1000,'currency':'sc'}]
		asks = [{'price':13.2,'volume':400,'currency':'btc'}]
		print(self.exchange_pair._check_bid_ask(bids, asks))

if __name__ == '__main__':
    unittest.main()
    
