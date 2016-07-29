import os
from context import yunbi_wrapper
import unittest

from context import _get_value

class BasicTestSuite(unittest.TestCase):
	def setUp(self):
		self.wrapper = yunbi_wrapper(_get_value('yunbi','apikey'), _get_value('yunbi','secret'))

	# def test_order_book(self):
	# 	print(self.wrapper.order_book())

	# def test_rate(self):
	# 	print(self.wrapper.btc_cny_rate())

	def test_ticker_pairs(self):
		pairs = ["sc"]
		print self.wrapper.ticker_pairs(pairs)


if __name__ == '__main__':
    unittest.main()