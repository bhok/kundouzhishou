import os
import logging
import logging.config
import httplib, urllib

dirpath=os.path.dirname(os.path.abspath(__file__))
logging.config.fileConfig(dirpath + '/../logging.conf')  
logger = logging.getLogger()

def log(msg):
	logger.log(msg)

def info(msg):
	logger.info(msg)

def pushover(app_id, content):
	logger.info(content)
	conn = httplib.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
		urllib.urlencode({
			"token": app_id,
			"user": "u4a6nc1byi7n8dgp3hktdd53w8er19",
			"message": content,
			"sound":"Persistent"
	}), { "Content-type": "application/x-www-form-urlencoded" })