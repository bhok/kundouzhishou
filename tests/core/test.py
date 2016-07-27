def _sort_test():
	orders = [{"price":"1"},{"price":"3"},{"price":"2"}]
	orders = sorted(orders, cmp=lambda x,y : cmp(x["price"], y["price"]),key=None,reverse=False)
	print(orders)

if __name__ == "__main__":
	_sort_test()
