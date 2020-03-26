import sma

# address of SMA
address = "0.0.0.0"

# your user password
password = "strongPassword"

# the right level
right = sma.RIGHT.USER

# create object
client = sma.WebConnect(address, right, password)

# authenticate with credentials
client.auth()

# check connection state
if not client.checkConnected():
	print("[!] Cannot authenticate to the server, check your credentials")
else:
	print("[+] Connected to SMA")
	print("[*] getting some data")

	# get the production counter from solar panel
	power_total = client.getValue(sma.KEYS.power_total)
	print("[*] Production Counter: %d%s" % (power_total, sma.KEYS.power_total["unit"]))

	# get the current production from solar panel
	pow_current = client.getValue(sma.KEYS.pow_current)
	print("[*] Current production: %d%s" % (pow_current, sma.KEYS.pow_current["unit"]))

	# Don't forget to disconnect from web server
	print("[+] Disconnecting..")
	if client.logout() == False:
		print("[!] Error in logout!")
	print("[.] Done.")