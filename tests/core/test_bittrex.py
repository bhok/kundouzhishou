import os
import sys

from context import bittrex
from context import conf
from context import core

from context import _get_value

import unittest

class BasicTestSuite(unittest.TestCase):
	def setUp(self):
		apikey = _get_value('bittrex','apikey')
		secret = _get_value('bittrex','secret')
		self.client = bittrex(apikey, secret)

	def test_get_markets(self):
		print self.client.get_markets()

	def test_get_orderbook(self):
		print self.client.get_orderbook("BTC-LTC",'both',50)

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(BasicTestSuite('test_get_orderbook'))
    unittest.TextTestRunner().run(suite)