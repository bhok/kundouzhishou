from context import yunbi
import conf
import os

class yunbi_wrapper():
	def __init__(self):
		dirpath=os.path.dirname(os.path.abspath(__file__))
		conf.init(dirpath + "/../account.ini")
		apikey = str(conf.get_value("yunbi", "apikey"))
		secret = str(conf.get_value("yunbi", "secret"))
		self.client = yunbi(apikey, secret)

	def balance(self):
		print self.client.get('members')


if __name__ == '__main__':
	wrapper = yunbi_wrapper()
	print(wrapper.balance())
