import sys
import os
sys.path.insert(0, os.path.abspath('../..'))

import core.conf as conf
import core.core as core

import core.exchange.yunbi as yunbi
import core.exchange.poloniex as poloniex
import core.exchange.bittrex as bittrex

import core.yunbi_wrapper as yunbi_wrapper
import core.poloniex_wrapper as poloniex_wrapper
import core.bittrex_wrapper as bittrex_wrapper


import core.exchange_pair as exchange_pair

def _get_value(section, key):
	dirpath = os.path.dirname(os.path.abspath(__file__))
	conf.init(dirpath + "/../../arbitrage/account.ini")
	return str(conf.get_value(section, key))