import os
from context import poloniex
from context import conf
from context import core

import unittest

class BasicTestSuite(unittest.TestCase):
	def setUp(self):
		dirpath=os.path.dirname(os.path.abspath(__file__))
		conf.init(dirpath + "/../account.ini")
		apikey = str(conf.get_value("poloniex", "apikey"))
		secret = str(conf.get_value("poloniex", "secret"))
		self.client = poloniex(apikey, secret)

	def test_return_ticker(self):
		ticker =  self.client.returnTicker()
		print(ticker)

	def test_return_balances(self):
		balances = self.client.returnBalances()
		print(balances)




if __name__ == '__main__':
    unittest.main()
