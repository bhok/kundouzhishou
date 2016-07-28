def _sort_test():
	orders = [{"price":"1"},{"price":"3"},{"price":"2"}]
	orders = sorted(orders, cmp=lambda x,y : cmp(x["price"], y["price"]),key=None,reverse=False)
	print(orders)

def _test():
	pair_map = {"sc":"sccny"}
	print "sc" in pair_map

if __name__ == "__main__":
	_test()