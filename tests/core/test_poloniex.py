import os
from context import poloniex
from context import conf
from context import core

from context import _get_value

import unittest

class BasicTestSuite(unittest.TestCase):
	def setUp(self):
		apikey = _get_value('poloniex','apikey')
		secret = _get_value('poloniex','secret')
		self.client = poloniex(apikey, secret)

	def test_return_ticker(self):
		ticker =  self.client.returnTicker()
		print(ticker)

	def test_return_balances(self):
		balances = self.client.returnBalances()
		print(balances)

	def test_return_order_books(self):
		print self.client.returnOrderBook("BTC_SC")

	def test_return_open_orders(self):
		print self.client.returnOpenOrders("BTC_SC")

if __name__ == '__main__':
    unittest.main()
