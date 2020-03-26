# Welcome to SMA API!

This is a simple data retrieving from **SMA SunnyBoy**

## Comptability
Tested on SunnyBoy 5.0 (1.3.17.R)

## Simple usage

```py
import sma
client = sma.WebConnect("192.168.0.10", sma.RIGHT.USER, "password")
client.auth()
pow_current = client.getValue(sma.KEYS.pow_current)
client.logout()
```

## Initialize
Start by import and instantiate the module using **WebConnect**

```py
import sma
client = sma.WebConnect("192.168.0.10", sma.RIGHT.USER, "password")
```

## Authenticate
Initialize the module using **auth()**

(return: **Boolean**)
```py
client.auth()
```

You can check if you are still authenticated using **checkConnected()**

(return: **Boolean**)
```py
client.checkConnected()
```

## Logout
You have to call logout before exiting the program

(return: **Boolean**)
```py
client.logout()
```

## Get Value
You can retrieve an instant value using **GetValue()**

Pass in argument the wanted key from **sma.KEY.key_name**

(return: **String**)

```py
value = client.getValue(sma.KEYS.power_total)
print(value)
```

You can use preset keys from the list bellow:
```py
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
```

## Get all instant values
Using **getAllKeys()** you can obtains all SMA value in JSON format

(return: **JSON**)

```py
data = client.getAllKeys()
print(data)
```
