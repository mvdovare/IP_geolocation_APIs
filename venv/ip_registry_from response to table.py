import requests
import json
import time
import csv


with open('ip_registry_response_jan20.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        ip_responses = [line.rstrip() for line in lines]

with open('result_table_ipregistry.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ip', 'isp', 'org_name', 'country_code', 'country_name', 'region_code', 'region_name', 'city', 'lat', 'lon', 'connection_type',
                  'is_cellular', 'is_proxy', 'is_vpn']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for ip in ip_responses:
        ip_json = json.loads(ip)
        region_long = ip_json['location']['region']['code']
        try:
            region_short = region_long[len(region_long) - 2:]
        except:
            region_short = ''
        writer.writerow(
            {'ip': ip_json['ip'],
             'isp': ip_json['connection']['organization'],
             'org_name': ip_json['company']['name'],
             'country_code': ip_json['location']['country']['code'],
             'country_name': ip_json['location']['country']['name'],
             'region_code': region_short,
             'region_name': ip_json['location']['region']['name'],
             'city': ip_json['location']['city'],
             'lat': ip_json['location']['latitude'],
             'lon': ip_json['location']['longitude'],
             'connection_type':ip_json['connection']['type'],
             'is_cellular': ip_json['carrier']['name'],
             'is_proxy': ip_json['security']['is_proxy'],
             'is_vpn': ''})




