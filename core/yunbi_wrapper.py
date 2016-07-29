from context import yunbi
import conf
import os
from copy import copy

interested_list = ["cny", "btc","eth"]

pairs_map = {"sc":"sccny"}

currency_pair_t = '{0}cny'
default_currency = 'cny'

class yunbi_wrapper():
	def __init__(self, apikey, secret):
		self.client = yunbi(apikey, secret)

	def name(self):
		return "yunbi"

	def btc_cny_rate(self):
		path = self.client.get_api_path('tickers') % "btccny"
		info = self.client.get_by_path(path, {}, False)
		return float(info["ticker"]["last"])

	# {"at":1469766261,"ticker":{"buy":"0.00438","sell":"0.0044","low":"0.00415","high":"0.00449","last":"0.00439","vol":"182339304.0"}}
	def ticker(self, currency):
		path = self.client.get_api_path('tickers') % self._get_pairs(currency) 
	 	info = self.client.get_by_path(path, {}, False)
	 	return {'price':float(info['ticker']['last']),'currency':currency}

	 # @return [{'price':xx,'curreny':xxx}, {}]
	def ticker_pairs(self, pairs):
	 	result = []
	 	for pair in pairs:
	 		result.append(self.ticker(pair))

	 	return result


	# "accounts":[{"currency":"cny","balance":"0.0","locked":"0.0"},{}]
	def balance(self):
		info = self.client.get('members')
		result = {}
		for item in info["accounts"]:
			for interested_key in interested_list:
				if item["currency"] == interested_key:
					result[interested_key] = item
					break

		return result

	# {u'created_at': u'2016-07-22T15:19:31Z', u'trades_count': 0, u'remaining_volume': u'1257807.0', u'price': u'0.00463', u'side': u'buy', u'volume': u'1257807.0', u'state': u'wait', u'ord_type': u'limit', u'avg_price': u'0.0', u'executed_volume': u'0.0', u'id': 221602221, u'market': u'sccny'}
	def order_book(self, currency, limit=100):
		info = self.client.get('order_book', params={'market': self._get_pairs(currency),'asks_limit': limit, 'bids_limit':limit})
		asks = self._parse_order(info["asks"])
		bids = self._parse_order(info["bids"])

		asks = sorted(asks, cmp=lambda x,y : cmp(x["price"], y["price"]),key=None,reverse=False)
		bids = sorted(bids, cmp=lambda x,y : cmp(x["price"], y["price"]),key=None,reverse=True)

		return bids,asks

	def _get_pairs(self, name):
		return str.format(currency_pair_t, name.lower())


	def _parse_order(self, orders):
		result = []
		for order in orders:
			find_tag = False
			for old_order in result:
				if old_order["price"] == order["price"]:
					find_tag = True
					old_order["volume"] = float(old_order["volume"]) + float(order["remaining_volume"])

			if not find_tag:
				result.append({"volume":float(order["remaining_volume"]), "price":float(order["price"]),"currency":default_currency})


		return result


if __name__ == '__main__':
	wrapper = yunbi_wrapper("ethcny")
	print(wrapper.order_book())