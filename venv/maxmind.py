import requests
import json
import time
from csv import DictReader

#https://api.ip2location.com/v2/?ip={IP_ADDRESS}&key={YOUR_API_KEY}&package={WS1|WS2|WS3|...|WS25}&addon={continent,country,region,city,geotargeting,country_groupings,time_zone_info}

#key = 'LXC0J6RWGI'
url = 'https://geoip.maxmind.com/geoip/v2.1/insights/'
ip = ''
#package = 'WS24'
final_list = []
final_txt = open ('Maxmind_response_test.txt', 'w', encoding='utf-8')
#account_id = '665213'
#license_key = 'RWuIx55nKYlPC2ZR'

with open('set_test.csv') as file:
    csv_obj = DictReader(file)
    for row in csv_obj:
        #print(url + row['IP'])
        result = requests.get(url + row['IP'], auth=(row['maxmind_account_id'], row['maxmind_license_key']))
        final_list.append(result.text)

for i in final_list:
    final_txt.write(i + '\n')
final_txt.close()
