import requests,json

url = 'https://api.mist.com/api/v1/sites/<your_Site_Here>/stats/clients'

headers = {
    'Content-Type': 'application/json',
    'Authorization': '<Your Token here>'
}

results = requests.get(url,headers=headers)
clients = json.loads(results.text)

client_protocols_count = {}
# This is the debug to see the whole JSON blob and client stats
#print(clients)

for c in clients:
  if c.get("proto","")!= "":
    if c["proto"] not in client_protocols_count:
        client_protocols_count[c["proto"]] = 1
    else:
        client_protocols_count[c["proto"]]+= 1

for k,v in client_protocols_count.items():
    print(v,":",k)
