import requests
import time
import json
import os
import httplib, urllib

dirpath=os.path.dirname(os.path.abspath(__file__))
yunbi_file_path = dirpath + "/yunbi.json"
bittrex_file_path = dirpath + "/bittrex.json"

def check_yunbi():
	page = requests.get('https://yunbi.com//api/v2/markets.json')
	if page.status_code != 200:
		return 
	new_data = json.loads(page.content)
	with open(yunbi_file_path, 'r') as rf:
		old_data = json.loads(rf.read())
		if len(old_data) > 0:
			for new_item in new_data:
				has_tag = False
				for old_item in old_data:
					if new_item["id"] == old_item["id"]:
						has_tag = True
						break

				if has_tag == False:
					_send_sms("yunbi: " + str(new_item))

	with(open(yunbi_file_path, 'wb')) as rf:
		rf.write(page.content)

def check_bittrex():
	page = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummaries')
	if page.status_code != 200:
		return 
	new_data = json.loads(page.content)['result']
	with open(bittrex_file_path, 'r') as rf:
		old_data = json.loads(rf.read())
		if len(old_data) > 0:
			for new_item in new_data:
				has_tag = False
				for old_item in old_data:
					if new_item["MarketName"] == old_item["MarketName"]:
						has_tag = True
						break

				if has_tag == False:
					_send_sms("bittrex: " + str(new_item['MarketName']))

	with(open(bittrex_file_path, 'wb')) as rf:
		rf.write(json.dumps(new_data))

def check_poloniex():
	_check_exchange('poloniex', 'https://poloniex.com/public?command=returnTicker')

def check_btc38():
	_check_exchange('btc38', 'http://api.btc38.com/v1/ticker.php?c=all&mk_type=cny')

def _check_exchange(name, url):
	filepath = dirpath + "/{0}.json".format(name)

	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
	}

	page = requests.get(url, headers=headers)
	if page.status_code != 200:
		print("http error code = " + str(page.status_code))
		return 
	new_data = json.loads(page.content)
	print(new_data)
	with open(filepath, 'r') as rf:
		old_data = json.loads(rf.read())
		if len(old_data) > 0:
			for new_item in new_data:
				has_tag = False
				for old_item in old_data:
					if new_item == old_item:
						has_tag = True
						break

				if has_tag == False:
					_send_sms(name + ": " + str(new_item))

	data = []
	for k,v in new_data.iteritems():
		data.append(k)

	# print(data)
	with(open(filepath, 'wb')) as rf:
		rf.write(json.dumps(data))


def _send_sms(content):
	print(content)
	conn = httplib.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
		urllib.urlencode({
			"token": "awxgc8snwec2nwu2sqpj5oc8bei6dz",
			"user": "u4a6nc1byi7n8dgp3hktdd53w8er19",
			"message": content,
			"sound":"Persistent"
	}), { "Content-type": "application/x-www-form-urlencoded" })
	response = conn.getresponse().read()

def _test():
	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
	}

	api_url = 'https://poloniex.com/public?command=returnTicker'
	resp = requests.get(api_url , headers=headers)
	print(resp.status_code)
	print(resp.content)

if __name__ == "__main__":
	check_btc38()
	check_yunbi()
	check_poloniex()
	check_bittrex()

	# _send_sms("test")
	# _test()
