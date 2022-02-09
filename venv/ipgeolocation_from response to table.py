import requests
import json
import time
import csv

with open('ipgeolocation_response_all_Jan20.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        ip_responses = [line.rstrip() for line in lines]

with open('result_table_ipgeolocation.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ip', 'isp', 'org_name', 'country_code', 'country_name', 'region_code', 'region_name', 'city', 'lat', 'lon' ,'connection_type',
                  'is_cellular', 'is_proxy', 'is_vpn']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for ip in ip_responses:
        ip_json = json.loads(ip)
        writer.writerow(
            {'ip': ip_json['ip'],
             'isp': ip_json['isp'],
             'org_name': ip_json['organization'],
             'country_code': ip_json['country_code2'],
             'country_name': ip_json['country_name'],
             'region_code': '',
             'region_name': ip_json['state_prov'],
             'city': ip_json['city'],
             'lat': ip_json['latitude'],
             'lon': ip_json['longitude'],
             'connection_type':ip_json['connection_type'],
             'is_cellular': '',
             'is_proxy': '',
             'is_vpn': ''})




