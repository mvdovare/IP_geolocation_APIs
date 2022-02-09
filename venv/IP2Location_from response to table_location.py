import requests
import json
import time
import csv

with open('IP2Location_location_Jan20.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        ip_responses = [line.rstrip() for line in lines]

with open('result_table_IP2Location_location_.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ip', 'isp', 'org_name', 'country_code', 'country_name', 'region_code', 'region_name', 'city', 'lat', 'lon' ,'connection_type',
                  'is_cellular', 'is_proxy', 'is_vpn']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for ip in ip_responses:
        ip_json = json.loads(ip)
        writer.writerow(
            {'ip': ip_json['IP'],
             'isp': ip_json['isp'],
             'org_name': ip_json['domain'],
             'country_code': ip_json['country_code'],
             'country_name': ip_json['country_name'],
             'region_code': '',
             'region_name': ip_json['region_name'],
             'city': ip_json['city_name'],
             'lat': ip_json['latitude'],
             'lon': ip_json['longitude'],
             'connection_type':ip_json['usage_type'],
             'is_cellular': ip_json['mobile_brand'],
             'is_proxy': '',
             'is_vpn': ''})




