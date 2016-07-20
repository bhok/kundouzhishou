import urllib2
import json
import hmac
import hashlib
import time
import urllib
import requests

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

    def get(self, cmd, params=None, is_try=None):
        path = self.get_api_path(cmd)
        return self.get_by_path(path, params, is_try)

    def get_by_path(self, path, params=None, is_try=None):
        verb = "GET"
        signature, query, params = self.auth.sign_params(verb, path, params)
        url = "%s%s?%s&signature=%s" % (BASE_URL, path, query, signature)

        print("url = " + url)

        if not is_try:
            response = requests.get(url)
            return self._get_content(response)
        

    def post(self, cmd, params=None, is_try=None):
        path = self.get_api_path(cmd)
        verb = "POST"
        signature, query, params = self.auth.sign_params(verb, path, params)
        url = "%s%s" % (BASE_URL, path)
        data = "%s&signature=%s" % (query, signature)
        params.update({'signature':signature})

        print "url=",url
        print "data=",data

        if not is_try:
            response = requests.post(url, data=params)
            return self._get_content(response)

    def get_api_path(self, name):
        path_pattern = API_PATH_DICT[name]
        return path_pattern % API_BASE_PATH

    def _get_content(self, response):
        print "code = ", response.status_code, "response = ",response.content
        return json.loads(response.content)

    def _get_headers(self):
        headers = {'Content-Type': 'my-app/0.0.1application/x-www-form-urlencoded', 'Accept':'application/json'}
        return headers

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
        return signature, query, params
