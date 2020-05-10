class Key:
	# status: 
	#	1725 -> offline
	#	307  -> online

	
	pow_current = {'tag': '6100_40263F00', 'unit': 'W'}
	power_total = {'tag': '6400_00260100', 'unit': 'W'}
	
	server_ip = {'tag': '6180_104A9A00'}
	server_dns = {'tag': '6180_104A9D00'}
	server_netmask = {'tag': '6180_104A9B00'}
	server_gatewy = {'tag': '6180_104A9C00'}

	powwer_ab = {'tag': '6380_40251E00'}
	powwer_b = {'tag': '6380_40451F00'}
	voltage_ab = {'tag': '6380_40451F00'}
	tide_ab = {'tag': '6380_40452100'}
	powwer_amp_ = {'tag': '6100_40465300', 'unit': 'A'}

	productivity_total = {'tag': '6400_00260100'}
	service_time = {'tag': '6400_00462E00', 'unit': 's'}
	injection_time = {'tag': '6400_00462F00', 'unit': 's'}

	ethernet_status = {'tag': '6180_084A9600', 'unit': 'status'}
	ethernet_counter_status = {'tag': '6180_084AAA00', 'unit': 'status'}
	ethernet_ip = {'tag': '6800_10AA6100'}
	ethernet_netmask = {'tag': '6800_10AA6200'}
	ethernet_gateway = {'tag': '6800_10AA6300'}
	ethernet_dns = {'tag': '6800_10AA6400'}

	wlan_strength = {'tag': '6100_004AB600'}
	wlan_ip = {'tag': '6180_104AB700'}
	wlan_netmask = {'tag': '6180_104AB800'}
	wlan_gateway = {'tag': '6180_104AB900'}
	wlan_dns = {'tag': '6180_104ABA00'}
	wlan_status = {'tag': '6180_084ABC00', 'unit': 'status'}
	wlan_scan_status = {'tag': '6180_084ABB00'}


	device_state = {'tag': '6180_084B1E00', 'unit' : 'W'}
	device_warning = {'tag': '6100_00411F00', 'unit': 'W'}
	device_error = {'tag': '6100_00412000', 'unit': 'W'}
