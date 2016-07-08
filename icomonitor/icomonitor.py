# -*- coding: utf-8 -*-

import requests
import time
import MySQLdb
import json
import configparser
import logging
import os
import re
import httplib, urllib
from lxml import html

dirpath=os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger('icomonitor')
hdlr = logging.FileHandler(dirpath + '/record.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)

id_file_path = "id.txt"

def tick():
	content = _get_content()
	lastid = 0
	if len(content) == 0:
		return
		
	with open(id_file_path,'r') as rf:
		lastid = int(rf.read())
	maxid = lastid

	tree = html.fromstring(content)
	nodes = tree.xpath('//*[@class="windowbg"]/b/span/a')
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
	content = ("tid = {0}, url = {1}, title = ".format(tid, url) + title)
	logger.debug(content)


def _send_sms(content):
	conn = httplib.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
		urllib.urlencode({
			"token": "apg2fy55cjiyzdnxfco7rf4njo1kdv",
			"user": "u4a6nc1byi7n8dgp3hktdd53w8er19",
			"message": content,
			"sound":"climb"
	}), { "Content-type": "application/x-www-form-urlencoded" })
	logger.debug(conn.getresponse())


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
	# _send_sms("hello jsy")