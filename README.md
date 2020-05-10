# Welcome to SMA API!

This is a simple data retrieving for **SMA SunnyBoy**

## Comptability
Tested on SunnyBoy 5.0 (1.3.17.R)

## Installation
```py
pip install SMA-SunnyBoy
```

## Simple usage

```py
from sma_sunnyboy import *
client = WebConnect("192.168.0.10", Right.USER, "password")
client.auth()
pow_current = client.get_value(Key.pow_current)
client.logout()
```

## Initialize
Start by import and instantiate the module using **WebConnect**

```py
from sma_sunnyboy import *
client = WebConnect("192.168.0.10", Right.USER, "password")
```

## Authenticate
Initialize the module using **auth()**

(return: **Boolean**)
```py
client.auth()
```

You can check if you are still authenticated using **check_connection()**

(return: **Boolean**)
```py
client.check_connection()
```

## Logout
You have to call logout before exiting the program

(return: **Boolean**)
```py
client.logout()
```

## Get all instant values
Using **get_all_keys()** you can obtains all SMA value in JSON format

(return: **JSON**)

```py
data = client.get_all_keys()
print(data)
```

## Get Value
You can retrieve an instant value using **get_value()**

Pass in argument the wanted key from **Key.key_name**

(return: **String**)

```py
value = client.get_value(Key.power_total)
print(value)
```

You can use preset keys from the list bellow:

| Tag                     | ID            | Unit   |
|-------------------------|---------------|--------|
| power_current           | 6100_40263F00 | W      |
| power_total             | 6400_00260100 | W      |
| server_ip               | 6180_104A9A00 |        |
| server_dns              | 6180_104A9D00 |        |
| server_netmask          | 6180_104A9B00 |        |
| server_gatewy           | 6180_104A9C00 |        |
| power_ab                | 6380_40251E00 |        |
| power_b                 | 6380_40451F00 |        |
| voltage_ab              | 6380_40451F00 |        |
| tide_ab                 | 6380_40452100 |        |
| power_amp_              | 6100_40465300 | A      |
| productivity_total      | 6400_00260100 |        |
| service_time            | 6400_00462E00 | s      |
| injection_time          | 6400_00462F00 | s      |
| ethernet_status         | 6180_084A9600 | status |
| ethernet_counter_status | 6180_084AAA00 | status |
| wlan_strength           | 6100_004AB600 |        |
| wlan_ip                 | 6180_104AB700 |        |
| wlan_netmask            | 6180_104AB800 |        |
| wlan_gateway            | 6180_104AB900 |        |
| wlan_dns                | 6180_104ABA00 |        |
| wlan_status             | 6180_084ABC00 | status |
| wlan_scan_status        | 6180_084ABB00 |        |
| device_state            | 6180_084B1E00 | W      |
| device_warning          | 6100_00411F00 | W      |
| device_error            | 6100_00412000 | W      |
