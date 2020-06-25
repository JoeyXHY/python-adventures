# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:25:58 2020

@author: 81552
"""


import urllib.request as r
import json
import numpy as np
from xpinyin import Pinyin
p = Pinyin()
filename = 'weather.json'    
data={}
dataf=list()
city=''
#得到每日平均最高最低温度
def getAverage(): 
    a=[]
    a1=[]
    a2=[]
    t.append(data['list'][0]['dt_txt'][5:10])
    for j in range(0,38):
        t1=data['list'][j]['dt_txt'][5:10]
        t2=data['list'][j+1]['dt_txt'][5:10]
        a1.append(data['list'][j]['main']['temp_max'])
        a2.append(data['list'][j]['main']['temp_min'])
        a.append(data['list'][j]['main']['temp'])
        if t1 != t2 : 
            A.append(np.median(a))
            MAX.append(max(a1))
            MIN.append(min(a2))
            del a1[:]
            del a2[:]
            del a[:]
            t.append(t2)        

            
def lineString(A,T):
    print('未来五天每日平均温度：')
    for k in range(0,5):
        if A[k]>=0 :
            print(str(T[k])+'|'+'='*int (A[k])+str(A[k])[0:2]+'℃')

def charWeather(s,x):
    for i in range(0,4):
        print('|'+ s +str(x[i])[0:5], end='')
    print('|'+s+str(x[4])[0:5]+'|')

                                                                               
def printf(T,A,M1,M2):   
    charWeather('2020年---', T)#时间 平均温度 最高气温 最低气温
    charWeather('平均气温: ', A)
    charWeather('最高气温: ', M1)
    charWeather('最低气温: ', M2)
    lineString(A,t)


def new():
    print('-'*40)
    print('请输入城市名：')
    city1=str(input())
    city=p.get_pinyin(city1, '')
    url  = 'http://api.openweathermap.org/data/2.5/forecast?q='+city+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
    data=r.urlopen(url).read().decode('utf-8')
    data = json.loads(data)    
    getAverage()
    printf(t,A,MAX,MIN)
    print('本周平均温度： '+str(np.mean([A[i] for i in range(0,5)]))[0:5]+'℃')
    high(t,MAX)
    save()
    

def read(cityname):
    with open(filename,'r',encoding='utf-8') as file:
        dataf=json.load(file)
        for j in range(0,len(dataf)):
            if dataf[j]['city']==str(cityname):
                print('-'*30)
                print('日期：  '+dataf[j]['date'])
                print('平均温度：  '+str(dataf[j]['temp_ave'])+'℃')
                print('最高温度：  '+str(dataf[j]['temp_max'])+'℃')
                print('最低温度：  '+str(dataf[j]['temp_min'])+'℃')
                print('-'*30)
    
                
                
                
def save():
    with open(filename,'r',encoding='utf-8') as file:
        dataf=json.load(file)
    data1={'city':city,'date':t[0],'temp_ave':A[0],'temp_max':MAX[0],'temp_min':MIN[0]}
    data2={'city':city,'date':t[1],'temp_ave':A[1],'temp_max':MAX[1],'temp_min':MIN[1]}
    data3={'city':city,'date':t[2],'temp_ave':A[2],'temp_max':MAX[2],'temp_min':MIN[2]}
    data4={'city':city,'date':t[3],'temp_ave':A[3],'temp_max':MAX[3],'temp_min':MIN[3]}
    data5={'city':city,'date':t[4],'temp_ave':A[4],'temp_max':MAX[4],'temp_min':MIN[4]}
    dataAdd=[data1,data2,data3,data4,data5]   
    dataf.extend(dataAdd)
    with open(filename,'w') as f_obj:
        json.dump(dataf,f_obj)
        
def high(date,a):
    dic=dict(zip(date,a))
    print('本周高温天：')
    print(list(filter(lambda x: x[1] <= 20, dic.items())))

A=[]
MAX=[]
MIN=[]
t=[]
print('查询新的天气预报扣”1“，查看历史记录扣”2“')
answer1 = int(input())

if answer1 == 1:
    new()
elif answer1 ==2:
    print('输入要搜索的城市名：',end='')
    city1 = str(input())
    cityname = p.get_pinyin(city1, '')
    read(cityname)
