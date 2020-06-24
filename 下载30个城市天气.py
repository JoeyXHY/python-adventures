#r'class="week"

import re
import requests
import json
citys=list()
filename="citys_weather.txt"
city_list=['shenzhen','beijing','shanghai','wuhan','tianjin',
           'guangzhou','zhuhai','foshan','guilin','xiamen','zhongshan','dalian',
           'guiyang','hangzhou','nanjing','kunming','tangshan','chengdu',
           'changchun','huizhou','yangzhou','changsha','lanzhou','jinan','jilin',
           'maoming','meizhou','haikou','jiangmen','london']
for city in city_list:
    url  = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
    #r = requests.get(url)
    demo=requests.get(url).text
    t1=float(re.findall('temp_min":(.*?),',demo)[0])
    t2=float(re.findall('temp_max":(.*?),',demo)[0])
    w=re.findall('"main":(.*?),',demo)[0]
    weather_dic={
        "city":city,
        "temp_min":t1,
        "temp_max":t2,
        "weather":w
        }
    with open(filename,'a',encoding='utf-8') as f_obj:
        json.dump(weather_dic,f_obj)
