import requests
import json
import time
from csv import DictReader

#https://api.ip2location.com/v2/?ip={IP_ADDRESS}&key={YOUR_API_KEY}&package={WS1|WS2|WS3|...|WS25}&addon={continent,country,region,city,geotargeting,country_groupings,time_zone_info}

#key = 'LXC0J6RWGI'
url = 'https://ip-geolocation.whoisxmlapi.com/api/v1'
ip = ''
#package = 'WS24'
final_list = []
final_txt = open ('XML_response.txt', 'w', encoding='utf-8')

with open('CSV_var_IP data set.csv') as file:
    csv_obj = DictReader(file)
    for row in csv_obj:
        params = dict(apiKey=row['xml_key'], ipAddress=row['IP'])
        result = requests.get(url, params=params)
        final_list.append(result.text)
        #result_json = result.json()
        #final_list.append(json.dumps(result_json))

for i in final_list:
    final_txt.write(i + '\n')
final_txt.close()
