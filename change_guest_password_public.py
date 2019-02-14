import requests
import json
import random
import string

url = 'https://api.mist.com/api/v1/sites/<site id>/wlans'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token <your token>'
}

results = requests.get(url, headers=headers)
wlans = json.loads(results.text)
wlanid = None
portal = None
for wlan in wlans:
    print(wlan["ssid"], ">", wlan["id"])
    if wlan["ssid"] == "<WLAN Name with Guest Portal>":
        wlanid = wlan["id"]
        portal = wlan["portal"]
if wlanid:
    thisisnew = ''.join(random.choice(string.ascii_letters) for _ in range(6))
    print("New Password is:", thisisnew)
    portal["password"] = thisisnew
    results = requests.put(url+"/{}".format(wlanid),
                           headers=headers, data='{"portal": ' + json.dumps(portal) + '}')
