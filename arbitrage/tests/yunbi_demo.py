import time
import os
import urllib2
from context import yunbi
from context import conf

dirpath=os.path.dirname(os.path.abspath(__file__))
conf.init(dirpath + "/../account.ini")
apikey = str(conf.get_value("yunbi", "apikey"))
secret = str(conf.get_value("yunbi", "secret"))

client = yunbi(access_key=apikey, secret_key=secret)

#demo of GET APIs

#get member info
print client.get('members')

#get markets
markets =  client.get('markets')
print "markets:", markets

#get tickers of each market
#market should be specified in url
print 
print "tickers in markets"
# for market in markets:
    # print client.get_by_path(client.get_api_path('tickers') % market['id'])

#get orders of each market
#market should be specified in params
print 
print "orders in markets"
for market in markets:
    print client.get('orders', {'market': market['id']})

#get order book
print client.get('order_book', params={'market': 'btccny'})

#get tardes
print client.get('trades', params={'market': 'btccny'})

#get my trades
print client.get('my_trades', params={'market': 'btccny'})

#get k line
print client.get('k', params={'market': 'btccny'})

#clear all orders in all markets
print client.post('clear')


#demo of POST APIs
#DANGROUS, you better use test account to debug POST APIs

"""
markets =  client.get(get_api_path('markets'))
print markets

#sell 10 dogecoins at price 0.01
params = {'market': 'dogcny', 'side': 'sell', 'volume': 10, 'price': 0.01}
res = client.post(get_api_path('orders'), params)
print res

#buy 10 dogecoins at price 0.001
params = {'market': 'dogcny', 'side': 'buy', 'volume': 10, 'price': 0.001}
res = client.post(get_api_path('orders'), params)
print res

#clear all orders in all markets
res = client.post(get_api_path('clear'))
print res
#delete a specific order by order_id

#first, let's create an sell order
#sell 10 dogecoins at price 0.01
params = {'market': 'dogcny', 'side': 'sell', 'volume': 12, 'price': 0.01}
res = client.post(get_api_path('orders'), params)
print res
order_id = res['id']

#delete this order
params = {"id": order_id}
res = client.post(get_api_path('delete_order'), params)
print res

#create multi orders
params = {'market': 'dogcny', 'orders': [{'side': 'buy', 'volume': 12, 'price': 0.0002}, {'side': 'sell', 'volume': 11, 'price': 0.01}]}
res = client.post(get_api_path('multi_orders'), params)
print res
"""