import os
import requests
from context import poloniex_wrapper
from context import conf
from context import core

from context import _get_value

import unittest

class BasicTestSuite(unittest.TestCase):
	def setUp(self):
		self.client = poloniex_wrapper("BTC_ETH", _get_value('poloniex','apikey'), _get_value('poloniex','secret'))

	def test_balance(self):
		print self.client.balance()

if __name__ == '__main__':
    unittest.main()
    
