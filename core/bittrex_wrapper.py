from context import bittrex 
import conf
import os

interested_list = ["btc","eth"]

currency_pair_t = 'BTC-{0}'
default_currency = 'btc'

class bittrex_wrapper():
	def __init__(self, apikey, secret):
		self.client = bittrex(apikey, secret)

	def name(self):
		return "bittrex"

	# {u'Notice': None, u'Created': u'2014-02-13T00:00:00', u'MinTradeSize': 1e-08, u'IsSponsored': None, u'BaseCurrencyLong': u'Bitcoin', u'MarketName': u'BTC-LTC', u'IsActive': True, u'LogoUrl': u'https://i.imgur.com/R29q3dD.png', u'MarketCurrencyLong': u'Litecoin', u'BaseCurrency': u'BTC', u'MarketCurrency': u'LTC'}
	def get_markets(self):
		result = []
		markets = self.client.get_markets()['result']
		for market in markets:
			result.append(market['MarketName'])
		return result

	# TODO []
	def balance(self):
		balances = self.client.get_balances()['result']
		return balances 

	# {u'BTC_RBY': {u'last': u'0.00019100', u'quoteVolume': u'9103.36897373', u'high24hr': u'0.00019225', u'isFrozen': u'0', u'highestBid': u'0.00018671', u'percentChange': u'-0.00650195', u'low24hr': u'0.00018502', u'lowestAsk': u'0.00019036', u'id': 81, u'baseVolume': u'1.73504955'},
	# @return [{'price':xx,'curreny':xxx}, {}]
	def ticker_pairs(self, pairs):
		return result

	# @response {u'message': u'', u'result': {u'sell': [{u'Rate': 0.006242, u'Quantity': 100.0}, {u'Rate': 0.00625, u'Quantity': 111.90677255}, {u'Rate': 0.00625171, u'Quantity': 0.37365784},
	# @return [{'volume':xxx,'price':xxx,'currency':xxx}, {}]
	def order_book(self, currency, depth = 5000):
		info = self.client.get_orderbook(self._get_pairs(currency), 'both', depth)['result']
		bids = []
		for bid_item in info["buy"]:
			bids.append({"volume":float(bid_item['Quantity']), "price":float(bid_item['Rate']), "currency":default_currency})

		asks = []
		for ask_item in info["sell"]:
			asks.append({"volume":float(ask_item['Quantity']), "price":float(ask_item['Rate']), "currency":default_currency})

		asks = sorted(asks, cmp=lambda x,y : cmp(x["price"], y["price"]),key=None,reverse=False)
		bids = sorted(bids, cmp=lambda x,y : cmp(x["price"], y["price"]),key=None,reverse=True)

		return bids,asks

	def _get_pairs(self, name):
		return str.format(currency_pair_t, name.upper())
