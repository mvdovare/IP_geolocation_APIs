import requests
import json
import time
import csv

with open('IP2Location_proxy_Jan20.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        ip_responses = [line.rstrip() for line in lines]

with open('result_table_IP2Location_proxy_.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ip', 'isp', 'country_code', 'country_name', 'region_code', 'region_name', 'city', 'lat', 'lon' ,'connection_type',
                  'is_cellular', 'is_proxy', 'is_vpn']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for ip in ip_responses:
        ip_json = json.loads(ip)
        writer.writerow(
            {'ip': ip_json['IP'],
             'is_proxy': ip_json['isProxy'],
             'is_vpn': ip_json['proxyType']})

        # параметры пересекаются  - is_proxy - Yes or No, but is_vpn - тип прокси, например VPN




