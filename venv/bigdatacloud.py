import requests
import json
import time

key = '90c8667680b84884999384ab3ce81360'
url = 'https://api.bigdatacloud.net/data/ip-geolocation-full'
ip = ''
final_list = []
final_txt = open ('bigdatacloud_response.txt', 'w', encoding='utf-8')

with open('IPs') as file:
    lines = file.readlines()
    IPs = [line.rstrip() for line in lines]

for ip in IPs:
    params = dict(key = key, ip = ip )
    result = requests.get(url, params=params)
    result_string = json.loads(result.text)
    final_list.append(json.dumps(result_string))

for i in final_list:
    final_txt.write(i + '\n')
final_txt.close()


