# -*- coding: utf-8 -*-

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

if __name__ == "__main__":
	logger.debug("test")