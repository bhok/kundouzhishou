import os
import logging
import logging.config
import httplib, urllib
import MySQLdb
import conf

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

def execute_sql(sql):
	dirpath = os.path.dirname(os.path.abspath(__file__))
	conf.init(dirpath + "/db.ini")

	section = 'mysql'
	host = conf.get_value(section, "host")
	username = conf.get_value(section, "username")
	password = conf.get_value(section, "password")
	database = conf.get_value(section, "database")
	db = MySQLdb.connect(host,username,password,database)
	cursor = db.cursor()
	
	# sql = db.escape_string(sql)
	
	logger.debug("execute sql:" + sql)

	try:
		cursor.execute(sql)
		db.commit()
	except Exception,err:
		print(err)
		db.rollback()

	db.close()
