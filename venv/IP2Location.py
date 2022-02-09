import requests
import json
import time

#https://api.ip2location.com/v2/?ip={IP_ADDRESS}&key={YOUR_API_KEY}&package={WS1|WS2|WS3|...|WS25}&addon={continent,country,region,city,geotargeting,country_groupings,time_zone_info}

key = 'LXC0J6RWGI'
url = 'https://api.ip2location.com/v2/'
ip = ''
package = 'WS24'
final_list = []
final_txt = open ('IP2Location.txt', 'w', encoding='utf-8')

with open('IPs') as file:
    lines = file.readlines()
    IPs = [line.rstrip() for line in lines]

for ip in IPs:
    params = dict(key=key, ip = ip , package = package)
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

