import requests
import json
import time
import csv


with open('Maxmind_response_Jan24.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        ip_responses = [line.rstrip() for line in lines]

with open('result_table_Maxmind.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ip', 'isp', 'country_code', 'country_name', 'region_code', 'region_name', 'city', 'lat', 'lon', 'connection_type',
                  'is_cellular', 'is_proxy', 'is_vpn']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for ip in ip_responses:
        ip_json = json.loads(ip)
        writer.writerow(
            {'ip': ip_json['ip'],
             'isp': ip_json['isp'],
             'country_code': ip_json['location']['country'],
             'country_name': '',
             'region_code': '',
             'region_name': ip_json['location']['region'],
             'city': ip_json['location']['city'],
             'lat': ip_json['location']['lat'],
             'lon': ip_json['location']['lng'],
             'connection_type':ip_json['connectionType'],
             'is_cellular': '',
             'is_proxy': '',
             'is_vpn': ''})




