# Welcome to SMA API!

This is a simple data retrieving from **SMA SunnyBoy**

## His history !!
After installed some solar panels, my father wanted to know how many their produce, then he ask me to retrieve these data, firstly I searched after an official API from SMA but nohting else hardware documentation, then I searched after some Gits made by user, but unfortunately, nothing worked for my beautifull SMA..
Well.. I love programming and digging in code source of other developper is always interesting,
and here I am :)

## Simple usage

```py
import sma
client= sma.WebConnect("192.168.0.10", sma.RIGHT.USER, "password")
client.auth()
pow_current= client.getValue(sma.KEYS.pow_current)
client.logout()
```

## Initialize
first initialize the module using **WebConnect**

exemple:
```py
import sma
client= sma.WebConnect("192.168.0.10", sma.RIGHT.USER, "password")
```

## Authenticate
first initialize the module using **auth()**
return **Boolean**
```py
client.auth()
```
but you can check if you are still authenticate using **checkConnected()**
return **Boolean**
```py
client.checkConnected()
```

## Logout
You must call logout before exiting the program
return **Boolean**
exemple:
```py
client.logout()
```

## Get Value
you can retrieve an instant value using **GetValue()**
pass in argument the wanted key from **sma.KEY.key_name**
return the value in String format

exemple:
```py
value= client.getValue(sma.KEYS.power_total)
print(value)
```

You can use preset keys from the list bellow:
(feel free to add your)
```py
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
```

## Get all instant values
Using **getAllKeys()** you can obtains all SMA value in JSON format
return **JSON**

exemple:
```py
data= client.getAllKeys()
print(data)
```

