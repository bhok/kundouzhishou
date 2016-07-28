# -*- coding: utf-8 -*-
import sys
import os

sys.path.insert(0, os.path.abspath('..'))

import core.conf as conf
import core.core as core

import core.yunbi_wrapper as yunbi_wrapper
import core.poloniex_wrapper as poloniex_wrapper
import core.exchange_pair as exchange_pair

PUSHOVER_APP_ID = "azh9bmnsj6soq29j1xsmz161neg9ui"

def run():
	exchange_yunbi = yunbi_wrapper("etccny", _get_value('yunbi','apikey'), _get_value('yunbi','secret'))
	exchange_poloniex = poloniex_wrapper("BTC_ETC", _get_value('poloniex','apikey'), _get_value('poloniex','secret'))

	ex_pair = exchange_pair(exchange_yunbi, exchange_yunbi, exchange_poloniex)
	info = ex_pair.run()

	if info != None and len(info) > 0:
		core.info(info)
		# _send_sms(info)

def _get_value(section, key):
	dirpath = os.path.dirname(os.path.abspath(__file__))
	conf.init(dirpath + "/account.ini")
	return str(conf.get_value(section, key))

def _send_sms(content):
	core.pushover(PUSHOVER_APP_ID, content)

if __name__ == "__main__":
	run()
	# _send_sms("test")

