import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from pricemonitor import pricemonitor


import unittest
import requests

class BasicTestSuite(unittest.TestCase):
	def setUp(self):
		self.monitor = pricemonitor.exchange_monitor()

	def test_check(self):
		new_info = [{"currency": "etc", "price": 0.0026334}, {"currency": "fct", "price": 0.00253}, {"currency": "sc", "price": 1.01e-06}, {"currency": "lbc", "price": 0.00073336}, {"currency": "amp", "price": 0.000178}]
		old_info = [{"currency": "etc", "price": 0.0029334}, {"currency": "fct", "price": 0.00252}, {"currency": "sc", "price": 1.02e-06}, {"currency": "lbc", "price": 0.00051336}, {"currency": "amp", "price": 0.000172}]
		print self.monitor._check(new_info, old_info, True)

	def test_record(self):
    	#  currency, new_price, old_price, bids, asks)
		bids = [{'price':11,'volume':10},{'price':10.5,'volume':100},{'price':9,'volume':1000}]
    	asks = [{'price':11.2,'volume':10},{'price':12,'volume':100},{'price':13,'volume':1000}]
    	# self.monitor._record("sc", 11.1, 9.7, bids, asks)

    	bids = [{'price':9.62,'volume':10},{'price':8.2,'volume':100},{'price':6.22,'volume':1000}]
    	asks = [{'price':10.3,'volume':10},{'price':12,'volume':100},{'price':15,'volume':1000}]
    	# self.monitor._record("sc", 9.7, 11.1, bids, asks)

	def test_ticker(self):
		self.monitor.ticker()

	# name,last_price,new_price,offset,bids_volumes, asks_volumes):
	def test_writeDB(self):
		bids = {}
		asks = {}
		price_offset=[0.1,0.2,0.3,0.5]
		for offset in price_offset:
			bids[offset] = 10
			asks[offset] = 9

		self.monitor._writeDB("test", 11, 10, -10, bids, asks)

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(BasicTestSuite('test_check'))
    unittest.TextTestRunner().run(suite)
