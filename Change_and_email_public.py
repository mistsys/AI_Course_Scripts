import requests
import json
import random
import string
import smtplib
from email.mime.text import MIMEText
from myconfig import GMAILID, GMAILPW

url = 'https://api.mist.com/api/v1/sites/<your site>/wlans'

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
    if wlan["ssid"] == "mist_test":
        wlanid = wlan["id"]
        portal = wlan["portal"]
if wlanid:
    thisisnew = ''.join(random.choice(string.ascii_letters) for _ in range(6))
    print("New Password is:", thisisnew)
    portal["password"] = thisisnew
    results = requests.put(url+"/{}".format(wlanid),
                           headers=headers, data='{"portal": ' + json.dumps(portal) + '}')
# Send Email ########

msg = MIMEText(
    "Guest Portal password has updated to '{}'".format(thisisnew), 'plain')
msg['Subject'] = "New Password for Guest Portal"
msg['From'] = "your_gmail@gmail.com"
msg['To'] = "your_gmail@gmail.com"

# Send the message via local SMTP server.
s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login(GMAILID, GMAILPW)
s.sendmail("your_gmail@gmail.com", ["your_gmail@gmail.com"], msg.as_string())
s.quit()
