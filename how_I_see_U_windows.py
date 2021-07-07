import json
import os
import time
import requests
import random
import string
import subprocess

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token al6tJNHvOSmJG3333######################################8amVKyyEP8dgJhPWd'
}

def get_clientrssi():
  
    results = subprocess.check_output(["netsh","wlan","show","interface"]).decode()

    lines = results.split('\r\n')

    d = {}
    for line in lines:
        if ':' in line:
            vals = line.split(':')
            if vals[0].strip() != '' and vals[1].strip() != '':
                d[vals[0].strip()] = vals[1].strip()

    for key in d.keys():
         
         if key == "Signal":

              return (d[key])

def get_windowsmac():

    results = subprocess.check_output(["netsh","wlan","show","interface"]).decode()
    lines = results.split('\r\n')

    d = {}
    for line in lines:
        if ': ' in line:
            vals = line.split(': ')
#           print(vals)
            if vals[0].strip() != '' and vals[1].strip() != '':
                d[vals[0].strip()] = vals[1].strip()

#print(next(d[key] for key in d.keys() if key == "Physical address"))
#line above could replace the code below

    for key in d.keys():					
         if key == "Physical address":
             client_mac = (d[key])

             return (client_mac)

# Main Section
client_mac = get_windowsmac()
# Get rid of colons
client_mac = client_mac.replace(":", "")
# Have the URL pull for my single client
url = ('https://api.mist.com/api/v1/sites/36879cd6-b569-11e5-8261-02e208b2d34f/stats/clients/{}'.format(client_mac))

client_rssi = 0
my_rssi = 0

while True:
    results = requests.get(url, headers=headers)
    client = json.loads(results.text)
# when pulling a single client you get a dictionary, if you pull all clients you will have a list of dictionaries

    client_rssi = get_clientrssi()
    my_rssi = client['rssi']
    print('Windows Signal', '=', client_rssi, '    ', my_rssi, '=', 'AP rssi')
    time.sleep(3)
