# -*- coding: utf-8 -*-

import requests
import time
import MySQLdb
import json
import configparser
import logging
import os
from lxml import html

dirpath=os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger('icomonitor')
hdlr = logging.FileHandler(dirpath + '/record.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)

def get_info():
	page = requests.get('https://bitcointalk.org/index.php?board=159.0')
	if page.status_code != 200:
		logger.info("status code : {0}".format(page.status_code))
		return

	tree = html.fromstring(page.content)
	urls = tree.xpath('//*[@id="bodyarea"]/div[2]/table/tbody/tr[13]/td[3]/b')
	print(urls)
	for url in urls:
		print(url)

if __name__ == "__main__":
	get_info()