import os
import requests
from context import poloniex_wrapper
from context import conf
from context import core

import unittest

class BasicTestSuite(unittest.TestCase):
	def setUp(self):
		self.client = poloniex_wrapper()

	def test_balance(self):
		print self.client.balance()

if __name__ == '__main__':
    unittest.main()
    
