import configparser
import os

config = configparser.ConfigParser()

def init(file_name):
	global config	
	config.read(file_name)

def get_value(section, key):
	global config
	return config.get(section,key)
