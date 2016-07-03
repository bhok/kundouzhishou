# -*- coding: utf-8 -*-

import requests
import time
import MySQLdb
import json
import configparser
import logging
import os

dirpath=os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger('siatrend')
hdlr = logging.FileHandler(dirpath + '/record.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)

def get_info():
	page = requests.get('http://explore.sia.tech/explorer')
	if page.status_code != 200:
		logger.info("status code : {0}".format(page.status_code))
		return

	# data = json.loads(page.text)

	# height = int(tree.xpath('//*[@id="height"]')[0].text)
	# total_coins = long(tree.xpath('//*[@id="totalCoins"]')[0].text)
	# difficulty = int(tree.xpath('//*[@id="difficulty"]')[0].text)
	# hashrate = int(tree.xpath('//*[@id="hashrate"]')[0].text)
	# timestamp = int(time.time()[0].text)
	# active_file_contracts = long(tree.xpath('//*[@id="activeFileContracts"]')[0].text)
	# total_file_contract_cost = long(tree.xpath('//*[@id="totalFileContractCost"]')[0].text)
	# total_file_contract_size = long(tree.xpath('//*[@id="totalFileContractSize"]')[0].text)
	# storage_proofs = long(tree.xpath('//*[@id="storageProofs"]')[0].text)

	# print(height,total_coins,difficulty,hashrate,timestamp,active_file_contracts,total_file_contract_cost,total_file_contract_size,storage_proofs)

	host = _get_cfg("host")
	username = _get_cfg("username")
	password = _get_cfg("password")
	database = _get_cfg("database")
	db = MySQLdb.connect(host,username,password,database)
	cursor = db.cursor()
	# sql = "insert into record(height,total_coin,diffculty,hashrate,timestamp,active_file_contracts,total_file_contract_cost,total_file_contract_size,storage_proof) values({0},{1},{2},{3},{4},{5},{6},{7},{8})".format(
		# height,total_coins,difficulty,hashrate,timestamp,active_file_contracts,total_file_contract_cost,total_file_contract_size,storage_proofs)
	
	logger.debug("record successful !")
	sql = "insert into json_record(data) value('{0}')".format(db.escape_string(str(page.text)))

	try:
		cursor.execute(sql)
		db.commit()
	except Exception,err:
		print(err)
		db.rollback()

	db.close()

def _get_cfg(field):
	config = configparser.ConfigParser()
	config.read('db.ini')
	return config.get("mysql",field)

if __name__ == "__main__":
	get_info()