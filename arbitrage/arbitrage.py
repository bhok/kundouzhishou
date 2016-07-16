# -*- coding: utf-8 -*-

import time
import MySQLdb
import json
import configparser
import logging
import logging.config
import os

import exchange

dirpath=os.path.dirname(os.path.abspath(__file__))
logging.config.fileConfig(dirpath + '/../logging.conf')  
logger = logging.getLogger()

def _test():
	exchange.hmm()

def _test_poloniex():
	apikey = str(_get_cfg("poloniex", "apikey"))
	secret = str(_get_cfg("poloniex", "secret"))
	polo_ex = poloniex(apikey, secret)
	print(polo_ex.returnBalances())

def _test_yunbi():
	apikey = str(_get_cfg("yunbi", "apikey"))
	secret = str(_get_cfg("yunbi", "secret"))
	print(apikey)

def _get_cfg(section, field):
	config = configparser.ConfigParser()
	config.read(dirpath + '/account.ini')
	return config.get(section,field)

if __name__ == "__main__":
	_test_yunbi()

