from poloniex_wrapper import poloniex_wrapper
from yunbi_wrapper import yunbi_wrapper

class exchange_pair():
	def __init__(self, currency_pair, ex_yunbi, exA, exB):
		self._ex_yunbi = ex_yunbi
		self._ex_A = exA
		self._ex_B = exB

    def run(self):
    	self._btc_cny_rate = self._ex_yunbi.btc_cny_rate()

    	self._balance_A = self._ex_A.balance()
    	self._balance_B = self._ex_B.balance()

    	A_bids, A_asks = self._ex_A.order_book()
    	B_bids, B_asks = self._ex_B.order_book()

    	self._check(A_bids,A_asks,B_bids,B_asks)

    def _check(self, A_bids, A_asks, B_bids, B_asks):

    	

    def _check_bid_ask(self, bids, asks):
    	bids = _transfor_currency(bids)
    	asks = _transfor_currency(asks)

    	
    	
    def _transfor_currency(self, order_list):
    	for order in order_list:
    		if order["currency"] == "btc":
    			order["price"] = order["price"] * self._btc_cny_rate
    			order["curreny"] = "cny"

    	return order_list
    	

