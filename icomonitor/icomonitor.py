# -*- coding: utf-8 -*-

import requests
import time
import MySQLdb
import json
import configparser
import logging
import logging.config
import os
import re
import httplib, urllib
from lxml import html

dirpath=os.path.dirname(os.path.abspath(__file__))
print(dirpath)
logging.config.fileConfig(dirpath + '/../logging.conf')  
logger = logging.getLogger()  
id_file_path = dirpath + "/id.txt"

def tick():
	content = _get_content()
	# content = _get_content_from_file()
	lastid = 0
	if len(content) == 0:
		return
		
	with open(id_file_path,'r') as rf:
		lastid = int(rf.read())
	maxid = lastid

	tree = html.fromstring(content)
	nodes = tree.xpath('//*[@class="windowbg"]/span/a')
	print(nodes)
	for node in nodes:
		url = node.get("href")
		text = node.text

		tid = int(re.match(r'(.*)=(\d*)', url).group(2))
		if tid > lastid:
			_findit(tid, url, text)

		# update maxid
		if tid > maxid:
			maxid = tid

	with open(id_file_path, 'wb+') as wf:
		wf.write(str(maxid))

def _findit(tid, url, title):
	content = ("tid = {0}\n url = {1}\n title = ".format(tid, url) + title)
	logger.info(content)
	_send_sms(content)


def _send_sms(content):
	conn = httplib.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
		urllib.urlencode({
			"token": "apg2fy55cjiyzdnxfco7rf4njo1kdv",
			"user": "u4a6nc1byi7n8dgp3hktdd53w8er19",
			"message": content,
			"sound":"climb"
	}), { "Content-type": "application/x-www-form-urlencoded" })
	response = conn.getresponse().read()
	logger.debug("send sms:" + response)


def _get_content():
	page = requests.get('https://bitcointalk.org/index.php?board=159.0')
	if page.status_code != 200:
		logger.info("req bitcointalk status code : {0}".format(page.status_code))
		return ""
	return page.content

def _get_content_from_file():
	f = open("page.html","rb+")
	content = f.read()
	f.close()
	return content

if __name__ == "__main__":
	tick()
	# _send_sms("url = xxx \n tid = xxx\n name=xxx")
