import os
from context import yunbi_wrapper
import unittest

class BasicTestSuite(unittest.TestCase):
	def setUp(self):
		self.wrapper = yunbi_wrapper()

	def test_order_book(self):
		print(self.wrapper.order_book())


if __name__ == '__main__':
    unittest.main()