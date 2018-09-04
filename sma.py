import requests, random, string, json, time

class RIGHT:
	USER= 'usr'
	INSTALLER= 'istl'

class KEYS:
	# status ?: 
	#	1725 -> offline
	#	307  -> online

	pow_current= {'tag': '6100_40263F00', 'unit': 'W'}
	power_total= {'tag': '6400_00260100', 'unit': 'W'}
	
	server_ip= {'tag': '6180_104A9A00'}
	server_dns= {'tag': '6180_104A9D00'}
	server_netmask= {'tag': '6180_104A9B00'}
	server_gatewy= {'tag': '6180_104A9C00'}

	powwer_ab= {'tag': '6380_40251E00'}
	powwer_b= {'tag': '6380_40451F00'}
	voltage_ab= {'tag': '6380_40451F00'}
	tide_ab= {'tag': '6380_40452100'}
	powwer_amp_= {'tag': '6100_40465300', 'unit': 'A'}

	productivity_total= {'tag': '6400_00260100'}
	service_time= {'tag': '6400_00462E00', 'unit': 's'}
	injection_time= {'tag': '6400_00462F00', 'unit': 's'}

	ethernet_status= {'tag': '6180_084A9600', 'unit': 'status'}
	ethernet_counter_status= {'tag': '6180_084AAA00', 'unit': 'status'}

	wlan_strength= {'tag': '6100_004AB600'}
	wlan_ip= {'tag': '6180_104AB700'}
	wlan_netmask= {'tag': '6180_104AB800'}
	wlan_gateway= {'tag': '6180_104AB900'}
	wlan_dns= {'tag': '6180_104ABA00'}
	wlan_status= {'tag': '6180_084ABC00', 'unit': 'status'}
	wlan_scan_status= {'tag': '6180_084ABB00'}


	device_state= {'tag': '6180_084B1E00', 'unit' : 'W'}
	device_warning= {'tag': '6100_00411F00', 'unit': 'W'}
	device_error= {'tag': '6100_00412000', 'unit': 'W'}
	
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
	ip= ''
	useSSL= False
	cookie= ''
	lsid= ''
	ssid= ''
	
	__user= ''
	__password= ''
	__url= ''
	__port= 80

	def __init__(self, ip, user, password, port=80, useSSL= False):
		self.ip= ip
		self.__user= user
		self.__password= password
		self.useSSL= useSSL
		self.port= port
		
		self.__url='http://'+self.ip
		if self.useSSL:
			self.__url='https://'+self.ip
		self.__url+=':'+str(port)

	# Login to the server
	def auth(self):
		self.lsid= self.__genSID()

		params= {
					'right': self.__user, 
					'pass': self.__password
				}
		headers= self.__getHeader(params)
	
		try:
			r = requests.post(self.__url+'/dyn/login.json', headers=headers, json=params)
		except Exception:
			return None

		json_data= json.loads(r.text)
		if 'err' in json_data:
			time.sleep(5)
			return self.auth()
		else:
			self.ssid= json_data['result']['sid']
			self.cookie= headers['Cookie']
			return True

	# Logout to the server
	def logout(self):
		params= {}
		headers= self.__getHeader(params)

		try: 
			r = requests.post(self.__url+'/dyn/logout.json?sid='+self.ssid, headers=headers, json=params)
			self.lsid= ''
			self.ssid= ''
			self.cookie= ''
		except Exception:
			return None

		json_data= json.loads(r.text)
		if 'err' in json_data:
			return False
		else:
			return not json_data['result']['isLogin']

	# Check connexion state
	def checkConnected(self):
		if self.lsid == '' or self.ssid == '' or self.cookie == '':
			return False

		params= {}
		headers= self.__getHeader(params)
		
		try:
			r = requests.post(self.__url+'/dyn/sessionCheck.json?sid='+self.ssid, headers=headers, json=params)
		except Exception:
			return None

		json_data= json.loads(r.text)
		if not 'result' in json_data:
			return False
		elif not 'cntDwnGg' in json_data['result']:
			return False

		return True

	# Get value by KEY
	def getValue(self, key):
		params= {
					'keys':  [key['tag']],
					'destDev': []
				}
		headers= self.__getHeader(params)
		
		try:
			r = requests.post(self.__url+'/dyn/getValues.json?sid='+self.ssid, headers=headers, json=params)
		except Exception:
			return None
	
		json_data= json.loads(r.text)
		if 'err' in json_data:
			return None
		else:
			val= json_data['result']['0156-76BD14A8'][key['tag']]['1'][0]['val']
			if val != None:
				return val
			else:
				return 0

	# Get all values
	def getAllKeys(self):

		params= {
					'destDev': []
				}
		headers= self.__getHeader(params)
		 
		try:
			r = requests.post(self.__url+'/dyn/getAllParamValues.json?sid='+self.ssid, headers=headers, json=params)
		except Exception:
			return None
		return r.text

	# Get all values from time range
	def getLogger(self, start, end):

		# select all data with a step of 5 minutes
		key= 28672

		params= {
					'destDev': [],
					'key': key,
					'tEnd': end,
					'tStart': start
				}

		headers= self.__getHeader(params)
		
		try:
			r = requests.post(self.__url+'/dyn/getLogger.json?sid='+self.ssid, headers=headers, json=params)
		except Exception:
			return None
		
		json_data= json.loads(r.text)
		
		if not 'result' in json_data: 
			return {}
		else:
			return json_data['result']['0156-76BD14A8']

	# ##################
	# Private functions
	# ##################
	def __genSID(self):
			return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
		
	def __getHeader(self, params=''):

		if self.cookie=='':
			return {
					'Host': self.ip,
					'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0',
					'Accept': 'application/json, text/plain, */*',
					'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
					'Accept-Encoding': 'gzip, deflate',
					'Referer': self.__url+'/',
					'Content-Type': 'application/json',
					'Content-Length': str(len(params)),
					'Cookie': 'tmhDynamicLocale.locale=%22en%22; user80=%7B%22role%22%3A%7B%22bitMask%22%3A2%2C%22title%22%3A%22usr%22%2C%22loginLevel%22%3A1%7D%2C%22username%22%3A861%2C%22sid%22%3A%22'+self.lsid+'%22%7D',
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
					'Cookie': self.cookie,
				}