from context import yunbi
from context import poloniex

dirpath=os.path.dirname(os.path.abspath(__file__))
conf.init(dirpath + "/../account.ini")

class exchange_pair():

	def __init__(self, currency_pair):
		apikey = str(conf.get_value("yunbi", "apikey"))
		secret = str(conf.get_value("yunbi", "secret"))
		self._yunbi_client = yunbi(apikey, secret)

		apikey = str(conf.get_value("poloniex", "apikey"))
		secret = str(conf.get_value("poloniex", "secret"))
		self._poloniex_client = poloniex(apikey, secret)

    def run(self):
    	return

    def _check(self):
    	

