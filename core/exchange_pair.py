import os
import sys
from poloniex_wrapper import poloniex_wrapper
from yunbi_wrapper import yunbi_wrapper

TRX_FEE = 0.003
MIN_EXPECT_PROFIT = 20

class exchange_pair():
	def __init__(self, ex_yunbi, exA, exB):
		self._ex_yunbi = ex_yunbi
		self._ex_A = exA
		self._ex_B = exB

	def run(self):
		self._btc_cny_rate = self._ex_yunbi.btc_cny_rate()

		self._balance_A = self._ex_A.balance()
		self._balance_B = self._ex_B.balance()

		A_bids, A_asks = self._ex_A.order_book()
		B_bids, B_asks = self._ex_B.order_book()

		target_volume, expect_income = self._check_bid_ask(A_bids, B_asks)
		if expect_income > MIN_EXPECT_PROFIT:
			info = "except profit=" + str(expect_income) + " volume=" + str(target_volume)
			return info
			# TODO check balance and sell
			# self._execute(target_volume, self._ex_A, self._ex_B)

		target_volume, expect_income = self._check_bid_ask(B_bids, A_asks)
		if expect_income > MIN_EXPECT_PROFIT:
			info = "except profit = " + str(expect_income) + " volume=" + str(target_volume)
			return info
			# TODO check balance and sell
			# self._execute(target_volume, self._ex_B, self._ex_A)

		return None

	def _check_bid_ask(self, bids, asks):
		bids = self._transfor_currency(bids)
		asks = self._transfor_currency(asks)

		expect_income = 0
		target_volume = 0

		while(True):
			if len(asks) == 0 or len(bids) == 0:
				break

			ask_order = asks[0]
			bid_order = bids[0]

			print("ask order = ", ask_order)
			print("bid_order = ", bid_order)

			price_gap = bid_order['price'] - ask_order['price']
			if not price_gap > 0:
				print('no price diffencees, break ...')
				break

			min_valume = min(ask_order['volume'], bid_order['volume'])
			expect_income += min_valume * price_gap * (1 - TRX_FEE)
			target_volume += min_valume

			ask_order["volume"] -= min_valume
			if not ask_order["volume"] > 0:
				print('remove ask')
				asks.remove(ask_order)

			bid_order['volume'] -= min_valume
			if not bid_order['volume'] > 0:
				print('remove volume')
				bids.remove(bid_order)

			print("new state, bids =", bids,' asks=', asks)
			print('expect_income = ', expect_income)
		return target_volume, expect_income

	# {'volume': 1725783.0459525, 'currency': 'btc', 'price': 1.02e-06}
	def _transfor_currency(self, order_list):
		for order in order_list:
			if order["currency"] == "btc":
				order["price"] = float(order["price"]) * self._btc_cny_rate
				order["currency"] = "cny"

		return order_list

	def _execute(self, volume, sell_exchange, buy_exchange):
		print('execute ...')

if __name__ == "__main__":
	print("main")    	

