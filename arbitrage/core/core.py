import os
import logging
import logging.config

dirpath=os.path.dirname(os.path.abspath(__file__))
logging.config.fileConfig(dirpath + '/../../logging.conf')  
logger = logging.getLogger()

def log(msg):
	logger.log(msg)

def info(msg):
	logger.info(msg)