import os
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


if __name__ == '__main__':
    unittest.main()
