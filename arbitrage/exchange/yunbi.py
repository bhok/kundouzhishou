import urllib2
import json
import hmac
import hashlib
import time
import urllib

BASE_URL = 'https://yunbi.com'

API_BASE_PATH = '/api/v2'
API_PATH_DICT = {
    # GET
    'members': '%s/members/me.json',
    'markets': '%s/markets.json',

    #market code required in url as {market}.json
    'tickers' : '%s/tickers/%%s.json',
    #market required in url query string as '?market={market}'
    'orders': '%s/orders.json',

    #order id required in url query string as '?id={id}'
    'order': '%s/order.json',

    #market required in url query string as '?market={market}'
    'order_book': '%s/order_book.json',

    #market required in url query string as '?market={market}'
    'trades': '%s/trades.json',

    #market required in url query string as '?market={market}'
    'my_trades': '%s/trades/my.json',

    'k': '%s/k.json',
    #clear orders in all markets
    'clear': '%s/orders/clear.json',

    #delete a specific order
    'delete_order': '%s/order/delete.json',

    #TODO multi orders API
    'multi_orders': '%s/orders/multi.json',
}

class yunbi():

    def __init__(self, access_key, secret_key):
        self.auth = Auth(access_key, secret_key)

    def get(self, cmd, params=None):
        path = self._get_api_path(cmd)
        verb = "GET"
        signature, query = self.auth.sign_params(verb, path, params)
        url = "%s%s?%s&signature=%s" % (BASE_URL, path, query, signature)

        print("url = " + url)

        resp = urllib2.urlopen(url)
        data = resp.readlines()
        if len(data):
            return json.loads(data[0])

    def post(self, cmd, params=None):
        path = self._get_api_path(cmd)
        verb = "POST"
        print params
        signature, query = self.auth.sign_params(verb, path, params)
        url = "%s%s" % (BASE_URL, path)
        data = "%s&signature=%s" % (query, signature)
        print data
        print url
        resp = urllib2.urlopen(url, data)
        data = resp.readlines()
        if len(data):
            return json.loads(data[0])

    def _get_api_path(self, name):
        path_pattern = API_PATH_DICT[name]
        return path_pattern % API_BASE_PATH

class Auth():
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key

    def urlencode(self, params):
        keys = params.keys()
        keys.sort()
        query = ''
        for key in keys:
            value = params[key]
            if key != "orders":
                query = "%s&%s=%s" % (query, key, value) if len(query) else "%s=%s" % (key, value)
            else:
                #this ugly code is for multi orders API, there should be an elegant way to do this
                d = {key: params[key]}
                for v in value:
                    ks = v.keys()
                    ks.sort()
                    for k in ks:
                        item = "orders[][%s]=%s" % (k, v[k])
                        query = "%s&%s" % (query, item) if len(query) else "%s" % item
        return query

    def sign(self, verb, path, params=None):
        query = self.urlencode(params)
        msg = "|".join([verb, path, query])
        signature = hmac.new(self.secret_key, msg=msg, digestmod=hashlib.sha256).hexdigest()
        return signature

    def sign_params(self, verb, path, params=None):
        if not params:
            params = {}
        params.update({'tonce': int(1000*time.time()), 'access_key': self.access_key})
        query = self.urlencode(params)
        signature = self.sign(verb, path, params)
        return signature, query
