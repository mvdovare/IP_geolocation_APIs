import requests
import json

apiKey = 'fb0baeb93c3e4925a4c9698b03e4f3ac'
url = 'https://api.ipgeolocation.io/ipgeo'
ip = ''
final_list = []
final_txt = open ('ipgeolocation_response_4.txt', 'w', encoding='utf-8')

with open('ipgeolocation_4') as file:
    lines = file.readlines()
    IPs = [line.rstrip() for line in lines]

for ip in IPs:
    params = dict(apiKey=apiKey, ip=ip)
    result = requests.get(url, params=params)
    final_list.append(result.text)

for i in final_list:
    final_txt.write(i + '\n')
final_txt.close()
#print(i)

#final_json = json.dumps(final_list)
#with open ('res.txt', 'w') as f:
#    for i in final_list:
#        f.write(i)

