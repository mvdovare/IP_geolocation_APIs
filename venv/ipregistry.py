import requests
import json
import time

# https://api.ipregistry.co/128.0.169.65?key=z2svfp18e7d0d4qr

key = 'z2svfp18e7d0d4qr'
url = 'https://api.ipregistry.co/'
ip = ''
final_list = []
final_txt = open ('ipregistry_response.txt', 'w', encoding='utf-8')

with open('IPs') as file:
    lines = file.readlines()
    IPs = [line.rstrip() for line in lines]

for ip in IPs:
    params = dict(key=key)
    result = requests.get(url + ip, params=params)
    result_json = result.json()
    result_json['ag'] = 15
    print(result_json)
    final_list.append(json.dumps(result_json))

for i in final_list:
    final_txt.write(i + "\n")
final_txt.close()
#print(i)

#final_json = json.dumps(final_list)
#with open ('res.txt', 'w') as f:
#    for i in final_list:
#        f.write(i)

