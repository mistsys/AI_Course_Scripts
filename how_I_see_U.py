import json
import os
import time
import requests
import random
import string

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token <your Token>'
}

def get_clientrssi():
    """Get the Clients POV for RSSI.
    Returns:
      integer of your clients RSSI from the AP.
    """
    input = os.popen(
        '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport -I')
    return int(''.join([x.split()[1] for x in input if 'agrCtlRSSI' in x]))


def get_macbookmac():
    """Get local macbooks en0 MAC address."""
    input = os.popen('ifconfig en0')
    return ''.join([x.split()[1] for x in input if 'ether' in x])


# Main Section
# Get rid of colons
client_mac = get_macbookmac()
client_mac = client_mac.replace(":", "")
# Have the URL pull for my single client
url = ('https://api.mist.com/api/v1/sites/<your site>/stats/clients/{}'.format(client_mac))

client_rssi = 0
my_rssi = 0

while True:
    results = requests.get(url, headers=headers)
    client = json.loads(results.text)
# when pulling a single client you get a dictionary, if you pull all clients you will have a list of dictionaries

    client_rssi = get_clientrssi()
    my_rssi = client['rssi']
    print('Macbook rssi', '=', client_rssi, '    ', my_rssi, '=', 'AP rssi')
    time.sleep(3)
