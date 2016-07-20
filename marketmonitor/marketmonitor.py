import requests
import time
import json
import os
import httplib, urllib

dirpath=os.path.dirname(os.path.abspath(__file__))
yunbi_file_path = dirpath + "/yunbi.json"
poloniex_file_path = dirpath + '/poloniex.json'

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

if __name__ == "__main__":
	check_yunbi()
	# _send_sms("test")
