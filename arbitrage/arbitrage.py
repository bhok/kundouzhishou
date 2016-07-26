# -*- coding: utf-8 -*-

import exchange.yunbi as yunbi
import exchange.poloniex as poloniex
import core.conf as conf
import core.core as core
import core.yunbi_wrapper as yunbi_wrapper
import core.poloniex_wrapper as poloniex_wrapper
import core.exchange_pair as exchange_pair

import httplib, urllib

def run():
	exchange_yunbi = yunbi_wrapper()
	exchange_poloniex = poloniex_wrapper()

	ex_pair = exchange_pair(exchange_yunbi, exchange_yunbi, exchange_poloniex)
	info = ex_pair.run()

	if info != None and len(info) > 0:
		core.info(info)
		_send_sms(info)

def _send_sms(content):
	conn = httplib.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
		urllib.urlencode({
			"token": "azh9bmnsj6soq29j1xsmz161neg9ui",
			"user": "u4a6nc1byi7n8dgp3hktdd53w8er19",
			"message": content,
			"sound":"Persistent"
	}), { "Content-type": "application/x-www-form-urlencoded" })
	response = conn.getresponse().read()

if __name__ == "__main__":
	run()

