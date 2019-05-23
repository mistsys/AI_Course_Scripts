import requests,json

url = 'https://api.mist.com/api/v1/sites/<your Site Here>/stats/clients'

headers = {
    'Content-Type': 'application/json',
    'Authorization': '<your Token Here'
}

results = requests.get(url,headers=headers)
os = json.loads(results.text)

client_protocols_count = {}
# Debug statement to see the whole JSON Blob
#print(os)

for c in os:
  if c.get("family", "") != "" and c.get("model", "") != "" and c.get("os", "") != "":
    dict_key = str(c["family"] + " " + c["model"] + "-" + c["os"])
    if dict_key not in client_protocols_count:
        client_protocols_count[dict_key] = 1
    else:
        client_protocols_count[dict_key]+= 1

for k,v in client_protocols_count.items():
    print(v,":",k)
