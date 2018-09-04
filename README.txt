# ##################
# Connexion
# ##################
webCo= sma.WebConnect("10.10.32.11", sma.RIGHT.USER, "dauvister")
	
if not webCo.auth():
	print("Failed to auth")
	return

print("Loged to the server")
print("local SID:\t" + webCo.lsid)
print("Connexion SID:\t" + webCo.ssid)
print("Cookie:\t" + webCo.cookie)

# ##################
# Print the current power production
# ##################

curr_pow= webCo.getValue(sma.KEYS.curr_pow)
total_pow= webCo.getValue(sma.KEYS.total_pow)

print("Current Power: " + str(curr_pow) + " " + str(sma.KEYS.curr_pow["unit"]))
print("Total Power: " + str(total_pow) + " " + str(sma.KEYS.total_pow["unit"]))


# ##################
# Get all instant values
# ##################

data= webCo.getAllKeys()
print("Data: " + data)

print("Total power: " + str(webCo.getValue(sma.KEYS.power_total)), end=' ')
print(sma.KEYS.power_total["unit"])
	
# ##################
# Get range value
# ##################
now= int(time.time())
delay = 60 * 10 # minutes"

start= now - delay
end= now
data= webCo.getLogger(start, end)
	
publisher= publish.Http()
for p in data:
	publisher.send({"Solar_Prod": int(p["v"])}, int(p["t"]))

# ##################
# Publish value to DB
# ##################

data= {
	"Solar_TotalProd": webCo.getValue(sma.KEYS.power_total),
	"Solar_Prod": webCo.getValue(sma.KEYS.pow_current)
	}

publisher= publish.Http()
publisher.send(data, 0)

# ##################
# Logout
# ##################
if webCo.logout():
	print("Done.")
else:
	print("Not logout!")