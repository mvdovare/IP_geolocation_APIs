import requests
import json
import time
import csv

with open('bigdatacloud_response_Jan21_string.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        ip_responses = [line.rstrip() for line in lines]

with open('result_table_bigdatacloud.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ip', 'isp', 'country_code', 'country_name', 'region_code', 'region_name', 'city', 'lat', 'lon' ,'connection_type',
                  'is_cellular', 'is_proxy', 'is_vpn']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for ip in ip_responses:
        ip_json = json.loads(ip)
        reg_long = ip_json['location']['isoPrincipalSubdivisionCode']
        reg_short = reg_long[len(reg_long) - 2: ]
        writer.writerow(
            {'ip': ip_json['ip'],
             'isp': ip_json['network']['carriers'][0]['organisation'],
             'country_code': ip_json['country']['isoAlpha2'],
             'country_name': ip_json['country']['name'],
             'region_code': reg_short,
             'region_name': ip_json['location']['isoPrincipalSubdivision'],
             'city': ip_json['location']['city'],
             'lat': ip_json['location']['latitude'],
             'lon': ip_json['location']['longitude'],
             'connection_type':'',
             'is_cellular': ip_json['hazardReport']['isCellular'],
             'is_proxy': ip_json['hazardReport']['isKnownAsProxy'],
             'is_vpn': ip_json['hazardReport']['isKnownAsVpn']})




