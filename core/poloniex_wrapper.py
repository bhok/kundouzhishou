from context import poloniex
import conf
import os

interested_list = ["btc","eth"]

currency_pair_t = 'BTC_{0}'
default_currency = 'btc'

class poloniex_wrapper():
	def __init__(self, apikey, secret):
		self.client = poloniex(apikey, secret)

	def name(self):
		return "poloniex"

	# {u'XVC': u'0.00000000', u'SRCC': u'0.00000000', u'EXE': u'0.00000000', u'WC': u'0.00000000', u'MIL': u'0.00000000', u'MIN': u'0.00000000', u'NOBL': u'0.00000000', u'NAS': u'0.00000000', u'NOTE': u'0.00000000', u'CCN': u'0.00000000', u'DRM': u'0.00000000', u'EXP': u'0.00000000', u'LQD': u'0.00000000', u'XBC': u'0.00000000', u'AXIS': u'0.00000000', u'XXC': u'0.00000000', u'SXC': u'0.00000000', u'SWARM': u'0.00000000', u'PRC': u'0.00000000', u'XUSD': u'0.00000000', u'OPAL': u'0.00000000', u'MYR': u'0.00000000', u'BBR': u'0.00000000', u'LTBC': u'0.00000000', u'LBC': u'0.00000000', u'NOXT': u'0.00000000', u'DRKC': u'0.00000000', u'SUN': u'0.00000000', u'BITUSD': u'0.00000000', u'MRC': u'0.00000000', u'DCR': u'0.00000000', u'GLB': u'0.00000000', u'WIKI': u'0.00000000', u'CHA': u'0.00000000', u'NXTI': u'0.00000000', u'FRAC': u'0.00000000', u'XPM': u'0.00000000', u'NTX': u'0.00000000', u'BTCS': u'0.00000000', u'IXC': u'0.00000000', u'URO': u'0.00000000', u'TAC': u'0.00000000', u'GPC': u'0.00000000', u'DASH': u'0.00000000', u'XAI': u'0.00000000', u'FVZ': u'0.00000000', u'YIN': u'0.00000000', u'QBK': u'0.00000000', u'GRCX': u'0.00000000', u'BTCD': u'0.00000000', u'CINNI': u'0.00000000', u'YACC': u'0.00000000', u'VIA': u'0.00000000', u'BURST': u'0.00000000', u'GIAR': u'0.00000000', u'XAP': u'0.00000000', u'SYS': u'0.00000000', u'MAID': u'0.00000000', u'APH': u'0.00000000', u'GML': u'0.00000000', u'MAX': u'0.00000000', u'BONES': u'0.00000000', u'NAV': u'0.00000000', u'HZ': u'0.00000000', u'INDEX': u'0.00000000', u'Q2C': u'0.00000000', u'XSV': u'0.00000000', u'GUE': u'0.00000000', u'USDE': u'0.00000000', u'BELA': u'0.00000000', u'BURN': u'0.00000000', u'FLT': u'0.00000000', u'SSD': u'0.00000000', u'FLO': u'0.00000000', u'IFC': u'0.00000000', u'METH': u'0.00000000', u'XSI': u'0.00000000', u'PTS': u'0.00000000', u'BLOCK': u'0.00000000', u'GRS': u'0.00000000', u'SILK': u'0.00000000', u'SHIBE': u'0.00000000', u'JUG': u'0.00000000', u'HUC': u'0.00000000', u'XDN': u'0.00000000', u'LSK': u'0.00000000', u'WOLF': u'0.00000000', u'SPA': u'0.00000000', u'MTS': u'0.00000000', u'AMP': u'0.00000000', u'UVC': u'0.00000000', u'GEO': u'0.00000000', u'FIBRE': u'0.00000000', u'BDG': u'0.00000000', u'ENC': u'0.00000000', u'LOVE': u'0.00000000', u'FLAP': u'0.00000000', u'BDC': u'0.00000000', u'BLU': u'0.00000000', u'MZC': u'0.00000000', u'FOX': u'0.00000000', u'FRK': u'0.00000000', u'SJCX': u'0.00000000', u'EFL': u'0.00000000', u'GRC': u'0.00000000', u'DSH': u'0.00000000', u'BNS': u'0.00000000', u'ECC': u'0.00000000', u'XEM': u'0.00000000', u'XRP': u'0.00000000', u'UTC': u'0.00000000', u'ULTC': u'0.00000000', u'USDT': u'0.00000000', u'MMXIV': u'0.00000000', u'LEAF': u'0.00000000', u'LTCX': u'0.00000000', u'BTS': u'0.00000000', u'VOOT': u'0.00000000', u'XCH': u'0.00000000', u'DOGE': u'0.00000000', u'XCN': u'0.00000000', u'XCR': u'0.00000000', u'XCP': u'0.00000000', u'RADS': u'0.00000000', u'MMC': u'0.00000000', u'BTC': u'0.00000000', u'BTM': u'0.00000000', u'EMC2': u'0.00000000', u'LCL': u'0.00000000', u'VOX': u'0.00000000', u'JLH': u'0.00000000', u'BCN': u'0.00000000', u'BLK': u'0.00000000', u'DVK': u'0.00000000', u'SLR': u'0.00000000', u'CRYPT': u'0.00000000', u'FZ': u'0.00000000', u'ACH': u'0.00000000', u'BCC': u'0.00000000', u'UTIL': u'0.00000000', u'GAME': u'0.00000000', u'CURE': u'0.00000000', u'TWE': u'0.00000000', u'BCY': u'0.00000000', u'NL': u'0.00000000', u'ETH': u'0.00000000', u'MUN': u'0.00000000', u'SMC': u'0.00000000', u'FLDC': u'0.00000000', u'CON': u'0.00000000', u'DGB': u'0.00000000', u'CLAM': u'0.00000000', u'FCT': u'0.00000000', u'N5X': u'0.00000000', u'PRT': u'0.00000000', u'CGA': u'0.00000000', u'GEMZ': u'0.00000000', u'OMNI': u'0.00000000', u'UIS': u'0.00000000', u'KDC': u'0.00000000', u'VRC': u'0.00000000', u'TOR': u'0.00000000', u'MAST': u'0.00000000', u'PMC': u'0.00000000', u'C2': u'0.00000000', u'QTL': u'0.00000000', u'BITS': u'0.00000000', u'EMO': u'0.00000000', u'FCN': u'0.00000000', u'VTC': u'0.00000000', u'CORG': u'0.00000000', u'SRG': u'0.00000000', u'PAWN': u'0.00000000', u'DIME': u'0.00000000', u'CC': u'0.00000000', u'XC': u'0.00000000', u'QORA': u'0.00000000', u'SYNC': u'0.00000000', u'LTC': u'0.00000000', u'RDD': u'0.00000000', u'FRQ': u'0.00000000', u'AUR': u'0.00000000', u'COMM': u'0.00000000', u'FZN': u'0.00000000', u'DNS': u'0.00000000', u'DIEM': u'0.00000000', u'ADN': u'0.00000000', u'MINT': u'0.00000000', u'AEON': u'0.00000000', u'XMR': u'0.00000000', u'1CR': u'0.00000000', u'MEC': u'0.00000000', u'HIRO': u'0.00000000', u'IOC': u'0.00000000', u'HVC': u'0.00000000', u'XDP': u'0.00000000', u'NAUT': u'0.00000000', u'ITC': u'0.00000000', u'PLX': u'0.00000000', u'H2O': u'0.00000000', u'NMC': u'0.00000000', u'KEY': u'0.00000000', u'SC': u'0.00000000', u'XMG': u'0.00000000', u'BITCNY': u'0.00000000', u'GDN': u'0.00000000', u'XHC': u'0.00000000', u'GNS': u'0.00000000', u'SHOPX': u'0.00000000', u'GOLD': u'0.00000000', u'NXT': u'0.00000000', u'MNTA': u'0.00000000', u'YC': u'0.00000000', u'XLB': u'0.00000000', u'RIC': u'0.00000000', u'LOL': u'0.00000000', u'AIR': u'0.00000000', u'HYP': u'0.00000000', u'CAI': u'0.00000000', u'BBL': u'0.00000000', u'WDC': u'0.00000000', u'ARCH': u'0.00000000', u'QCN': u'0.00000000', u'DIS': u'0.00000000', u'PPC': u'0.00000000', u'HUGE': u'0.00000000', u'SOC': u'0.00000000', u'LC': u'0.00000000', u'EAC': u'0.00000000', u'DAO': u'0.00000000', u'XPB': u'0.00000000', u'X13': u'0.00000000', u'GAP': u'0.00000000', u'CYC': u'0.00000000', u'BOST': u'0.00000000', u'YANG': u'0.00000000', u'MMNXT': u'0.00000000', u'FAC': u'0.00000000', u'NSR': u'0.00000000', u'MON': u'0.00000000', u'NBT': u'0.00000000', u'AC': u'0.00000000', u'BALLS': u'0.00000000', u'SUM': u'0.00000000', u'RBY': u'0.00000000', u'GPUC': u'0.00000000', u'AERO': u'0.00000000', u'CNOTE': u'0.00000000', u'NEOS': u'0.00000000', u'HOT': u'0.00000000', u'RZR': u'0.00000000', u'STR': u'0.00000000', u'PAND': u'0.00000000', u'CNMT': u'0.00000000', u'ABY': u'0.00000000', u'CNL': u'0.00000000', u'MRS': u'0.00000000', u'CACH': u'0.00000000', u'BANK': u'0.00000000', u'PINK': u'0.00000000', u'MCN': u'0.00000000', u'DICE': u'0.00000000', u'LGC': u'0.00000000', u'JPC': u'0.00000000', u'SQL': u'0.00000000', u'UNITY': u'0.00000000', u'XST': u'0.00000000', u'EBT': u'0.00000000', u'eTOK': u'0.00000000', u'SDC': u'0.00000000', u'NRS': u'0.00000000', u'TRUST': u'0.00000000', u'POT': u'0.00000000', u'PIGGY': u'0.00000000'}
	def balance(self):
		result = {}
		info = self.client.returnBalances()
		for interested_key in interested_list:
			result[interested_key] = {"balance":info[interested_key.upper()],'locked':0}
		return result

	# {u'BTC_RBY': {u'last': u'0.00019100', u'quoteVolume': u'9103.36897373', u'high24hr': u'0.00019225', u'isFrozen': u'0', u'highestBid': u'0.00018671', u'percentChange': u'-0.00650195', u'low24hr': u'0.00018502', u'lowestAsk': u'0.00019036', u'id': 81, u'baseVolume': u'1.73504955'},
	# @return [{'price':xx,'curreny':xxx}, {}]
	def ticker_pairs(self, pairs):
		result = []
		info =  self.client.returnTicker()

		for pair in pairs:
			key = self._get_pairs(pair)
			result.append({'price':float(info[key]['last']), 'currency':pair})

		return result

	# @response {u'bids': [[u'0.00000100', 2911945.7967204], [u'0.00000099', 1475490.160369], [u'0.00000098', 12760756.47514],
	# @return [{'volume':xxx,'price':xxx,'currency':xxx}, {}]
	def order_book(self, currency, depth = 5000):
		info = self.client.returnOrderBook(self._get_pairs(currency), depth)
		bids = []
		for bid_item in info["bids"]:
			bids.append({"volume":float(bid_item[1]), "price":float(bid_item[0]), "currency":default_currency})

		asks = []
		for ask_item in info["asks"]:
			asks.append({"volume":float(ask_item[1]), "price":float(ask_item[0]), "currency":default_currency})

		asks = sorted(asks, cmp=lambda x,y : cmp(x["price"], y["price"]),key=None,reverse=False)
		bids = sorted(bids, cmp=lambda x,y : cmp(x["price"], y["price"]),key=None,reverse=True)

		return bids,asks

	def _get_pairs(self, name):
		return str.format(currency_pair_t, name.upper())

if __name__ == '__main__':
	wrapper = poloniex_wrapper()
	print(wrapper.order_book())