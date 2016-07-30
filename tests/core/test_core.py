import unittest
import requests

from context import core

class BasicTestSuite(unittest.TestCase):
    def test_execute_sql(self):
    	sql = "show tables;"
    	sql = "insert into price_monitor(`name`,`last_price`,`new_price`,`offset`,`volume_inc_10`, `volume_dec_10`,`volume_inc_20`, `volume_dec_20`,`volume_inc_30`,`volume_dec_30`,`volume_inc_50`,`volume_dec_50`) values('test',11,10,-10,9,10,9,10,9,10,9,10)"
    	sql = "select count(*) from siatrend"
    	sql = "insert into test(`content`) value('%s')" % ("hehe")
    	# sql = "insert into test(`content`) values(10)"
    	core.execute_sql(sql)

if __name__ == '__main__':
    unittest.main()
