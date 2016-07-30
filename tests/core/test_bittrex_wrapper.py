import os
import requests
from context import bittrex_wrapper
from context import conf
from context import core

from context import _get_value

import unittest

class BasicTestSuite(unittest.TestCase):
	def setUp(self):
		self.client = bittrex_wrapper(_get_value('bittrex','apikey'), _get_value('bittrex','secret'))

	def test_get_markets(self):
		print self.client.get_markets()

	def test_balance(self):
		print self.client.balance()

	def test_ticker_pairs(self):
		pairs = ["sc","etc"]
		print self.client.ticker_pairs(pairs)

	def test_order_book(self):
		bids,asks = self.client.order_book('LTC')
		print "bids=",bids
		print "asks=",asks

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(BasicTestSuite('test_order_book'))
    unittest.TextTestRunner().run(suite)
    
