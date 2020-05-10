import time
import random
import string
import json
import requests

from .right import Right
from .key import Key
	
# #######################
# Other useful  files
# #######################
#
# login: '/login.json',
# logout: '/logout.json',
# getTime: '/getTime.json',
# getValues: '/getValues.json',
# getAllOnlValues: '/getAllOnlValues.json',
# getAllParamValues: '/getAllParamValues.json',
# setParamValues: '/setParamValues.json',
# getWebSrvConf: '/getWebSrvConf.json',
# getEventsModal: '/getEvents.json',
# getEvents: '/getEvents.json',
# getLogger: '/getLogger.json',
# getBackup: '/getConfigFile.json',
# loginGridGuard: '/loginSR.json',
# sessionCheck: '/sessionCheck.json',
# setTime: '/setTime.json',
# backupUpdate: 'input_file_backup.htm',
# fwUpdate: 'input_file_update.htm',
# SslCertUpdate: 'input_file_ssl.htm'

class WebConnect:
	"""The WebConnect object contains all methods to handle SMA features

	:return: A new instance of WebConnect
	:rtype: WebConnect
	"""
	ip = None
	use_ssl = False
	cookie = None
	lsid = None
	ssid = None
	
	__user = None
	__password = None
	__url = None
	__port = 80
	__serial = None

	def __init__(self, ip: str, user: Right, password: str, port=80, use_ssl=False):
		"""Initialize a new WebConnect object

		:param ip: The IP of the SMA
		:type ip: str
		:param user: The username to use (see in the Right class)
		:type user: str
		:param password: The password to use
		:type password: str
		:param port: The SMA web port, defaults to 80
		:type port: int, optional
		:param use_ssl: Should establish use SSL, defaults to False
		:type use_ssl: bool, optional
		"""
		self.ip = ip
		self.__user = user
		self.__password = password
		self.use_ssl = use_ssl
		self.port = port
		
		self.__url = 'http://'+self.ip
		if self.use_ssl:
			self.__url = 'https://'+self.ip

		self.__url+= ':'+str(port)

	def auth(self):
		"""Establish a new connexion

		:return: Is the authentication is successful
		:rtype: bool
		"""
		self.lsid = self.__gen_sid()

		params = {
					'right': self.__user, 
					'pass': self.__password
				}
		headers = self.__get_header(params)
	
		try:
			r = requests.post(self.__url + '/dyn/login.json', headers=headers, json=params)
		except Exception:
			return None

		json_data= json.loads(r.text)
		if 'err' in json_data:
			time.sleep(5)
			return self.auth()
		else:
			self.ssid = json_data['result']['sid']
			self.cookie = headers['Cookie']
			return True

	def logout(self):
		"""Logout and clear connexion

		:return: Is the logout is successful
		:rtype: bool
		"""
		params = {}
		headers = self.__get_header(params)

		try: 
			r = requests.post(self.__url + '/dyn/logout.json?sid=' + self.ssid, headers=headers, json=params)
		except Exception:
			return False

		json_data = json.loads(r.text)
		if 'err' in json_data:
			return False
		else:
			self.lsid = None
			self.ssid = None
			self.cookie = None
			return not json_data['result']['isLogin']

	def check_connection(self):
		"""Check connexion state

		:return: Is connected
		:rtype: bool
		"""
		if self.lsid is None or self.ssid is None or self.cookie is None:
			return False

		params = {}
		headers = self.__get_header(params)
		
		try:
			r = requests.post(self.__url + '/dyn/sessionCheck.json?sid=' + self.ssid, headers=headers, json=params)
		except Exception:
			return None

		json_data = json.loads(r.text)
		if not 'result' in json_data:
			return False
		elif not 'cntDwnGg' in json_data['result']:
			return False

		return True

	def get_value(self, key: Key):
		"""Get a specific value

		:param key: The key to retrieve values from (see in the Key class)
		:type key: dict
		:return: A list of values
		:rtype: str | int | None
		"""
		# TODO: Check return type
		params = {
					'keys':  [key['tag']],
					'destDev': []
				}
		headers = self.__get_header(params)
		
		try:
			r = requests.post(self.__url + '/dyn/getValues.json?sid=' + self.ssid, headers=headers, json=params)
		except Exception:
			return None
	
		json_data = json.loads(r.text)
		if 'err' in json_data:
			return None
		else:
			self.__serial = list(json_data['result'].keys())[0]
			val = json_data['result'][self.__serial][key['tag']]['1'][0]['val']
			if val != None:
				return val
			else:
				return 0

	def get_all_keys(self):
		"""Get all keys from the & API

		:return: All keys
		:rtype: dict
		"""

		params = { 'destDev': [] }
		headers = self.__get_header(params)
		 
		try:
			r = requests.post(self.__url + '/dyn/getAllParamValues.json?sid=' + self.ssid, headers=headers, json=params)
			json_data = json.loads(r.text)
			self.__serial = self.__serial = list(json_data['result'].keys())[0]
			return json_data['result'][self.__serial]	
		except Exception:
			return None

	def get_logger(self, start: int, end: int):
		"""Get solar production in the timestamp range

		:param start: The start timestamp
		:type start: int
		:param end: The end timestamp
		:type end: int
		:return: All values in the timestamp range
		:rtype: list
		"""

		# select all data with a step of 5 minutes
		key = 28672

		params = {
					'destDev': [],
					'key': key,
					'tEnd': end,
					'tStart': start
				}

		headers = self.__get_header(params)
		
		try:
			r = requests.post(self.__url + '/dyn/getLogger.json?sid=' + self.ssid, headers=headers, json=params)
		except Exception:
			return None
		
		json_data = json.loads(r.text)
		
		if not 'result' in json_data: 
			return {}
		else:
			self.__serial = list(json_data['result'].keys())[0]
			return json_data['result'][self.__serial]

	def __gen_sid(self):
		"""Generate a random SID

		:return: A new SID
		:rtype: str
		"""
		return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))

	def get_serial(self):
		return self.__serial

	def __get_header(self, params=list()):
		"""Get an HTML header

		:param params: Parameters who will be sent, defaults to list()
		:type params: str, optional
		:return: The HTML header to use
		:rtype: dict
		"""
		if self.cookie is None:
			return {
					'Host': self.ip,
					'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0',
					'Accept': 'application/json, text/plain, */*',
					'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
					'Accept-Encoding': 'gzip, deflate',
					'Referer': self.__url+'/',
					'Content-Type': 'application/json',
					'Content-Length': str(len(params)),
					'Cookie': 'tmhDynamicLocale.locale=%22en%22; user80=%7B%22role%22%3A%7B%22bitMask%22%3A2%2C%22title%22%3A%22usr%22%2C%22loginLevel%22%3A1%7D%2C%22username%22%3A861%2C%22sid%22%3A%22' + self.lsid + '%22%7D',
				 }
		else:
			return {
					'Host': self.ip,
					'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0',
					'Accept': 'application/json, text/plain, */*',
					'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
					'Accept-Encoding': 'gzip, deflate',
					'Referer': self.__url+'/',
					'Content-Type': 'application/json',
					'Content-Length': str(len(params)),
					'Cookie': '',
				}
