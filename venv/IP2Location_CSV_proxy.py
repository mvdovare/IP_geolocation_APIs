import requests
import json
import time
from csv import DictReader

#https://api.ip2location.com/v2/?ip={IP_ADDRESS}&key={YOUR_API_KEY}&package={WS1|WS2|WS3|...|WS25}&addon={continent,country,region,city,geotargeting,country_groupings,time_zone_info}

#key = 'LXC0J6RWGI'
url = 'https://api.ip2proxy.com/'
ip = ''
#package = 'WS24'
final_list = []
final_txt = open ('IP2Location_proxy.txt', 'w', encoding='utf-8')

with open('CSV_var_IP data set.csv') as file:
    csv_obj = DictReader(file)
    for row in csv_obj:
        params = dict(key=row['IP2Location_proxyKey'], ip=row['IP'], package=row['proxy_package'])
        result = requests.get(url, params=params)
        result_json = result.json()
        result_json['IP'] = row['IP']
        final_list.append(json.dumps(result_json))

for i in final_list:
    final_txt.write(i + '\n')
final_txt.close()
