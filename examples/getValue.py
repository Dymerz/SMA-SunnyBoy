from sma_sunnyboy import WebConnect, Key, Right


address = "0.0.0.0" 			# address of SMA
password = "strongPassword"		# your user password
right = Right.USER				# the connexion level

# create object
client = WebConnect(address, right, password)

# authenticate with credentials
client.auth()

# check connection state
if not client.check_connection():
	print("[!] Cannot authenticate to the server, check your credentials")
else:
	print("[+] Connected to SMA")
	print("[*] getting some data")

	# get the production counter from solar panel
	power_total = client.get_value(Key.power_total)
	print("[*] Production Counter: %d%s" % (power_total, Key.power_total["unit"]))

	# get the current production from solar panel
	power_current = client.get_value(Key.power_current)
	print("[*] Current production: %d%s" % (power_current, Key.power_current["unit"]))

	# Don't forget to disconnect from web server
	print("[+] Disconnecting..")
	if client.logout() is False:
		print("[!] Error in logout!")
	print("[+] Done.")
