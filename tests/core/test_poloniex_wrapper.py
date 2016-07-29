import os
import requests
from context import poloniex_wrapper
from context import conf
from context import core

from context import _get_value

import unittest

class BasicTestSuite(unittest.TestCase):
	def setUp(self):
		self.client = poloniex_wrapper(_get_value('poloniex','apikey'), _get_value('poloniex','secret'))

	def test_balance(self):
		print self.client.balance()

	def test_ticker_pairs(self):
		pairs = ["sc","etc"]
		print self.client.ticker_pairs(pairs)

	def test_order_book(self):
		bids,asks = self.client.order_book('sc')

if __name__ == '__main__':
    unittest.main()
    
