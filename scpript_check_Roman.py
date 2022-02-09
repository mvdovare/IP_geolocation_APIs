# здесь в ip_responses содержится построчно респонсы с апишки.
with open('D:\pycharm\IP Geolocation API\\venv\Maxmind_response_Jan24.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    ip_responses = [line.rstrip() for line in lines]

# 3 строки ниже наверное лишние, раз они у меня дублируются в коде ниже
with open('D:\pycharm\IP Geolocation API\\venv\maxmind DBs\GeoIP2-ISP-CSV_20220208\GeoIP2-ISP-Blocks-IPv4.csv',
          'r', newline='', encoding='utf-8') as csvfile:
    data_from_csv = csv.DictReader(csvfile)  # это CSV в котором поле "network" содержит маску подсети в виде  1.0.128.0/17  и остальные данные в других полях. Тут ~600 тыс строк.

with open('result_table_Maxmind_comply.csv', 'w', newline='', encoding='utf-8') as csvfile:  # открываю цсв чтобы записывать данные в случае если мой IP попадает в определенную подсеть.
    fieldnames = ['ip', 'isp', 'org_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for ip in ip_responses:  # перебираю свой датасет респонсов с АПИшки.
        ip_json = json.loads(ip) # каждый респоснс в виде json и я его тут преобразовую, чтобы потом находить нужный тег
        with open('D:\pycharm\IP Geolocation API\\venv\maxmind DBs\GeoIP2-ISP-CSV_20220208\GeoIP2-ISP-Blocks-IPv4.csv',
                  'r', newline='', encoding='utf-8') as csvfile:
            data_from_csv = csv.DictReader(csvfile) # это CSV в котором поле "network" содержит маску подсети в виде  1.0.128.0/17  и остальные данные в других полях. Тут ~600 тыс строк.
            for row in data_from_csv:  # тут перебираю все 600тыс масок подсети, чтобы найти ту, в которую попадает мой IP из респосна с АПИ.
                try:
                    if ipaddress.IPv4Address(ip_json['traits']['ip_address']) in ipaddress.IPv4Network(row['network']): # здесь проверяю попадает ли мой IP в эту подсеть
                        writer.writerow(
                            {'ip': ip_json['traits']['ip_address'],
                             'isp': row['isp'],
                             'org_name': row['organization']})
                except Exception as e:
                    print(e)
