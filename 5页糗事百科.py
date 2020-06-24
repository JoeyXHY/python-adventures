# -*- coding: utf-8 -*-
"""
Created on Fri May 15 16:34:12 2020

@author: 81552
"""

import requests
import re
from bs4 import BeautifulSoup
filename='糗事百科.txt'
mf=list()

url='https://www.qiushibaike.com/text/'
for i in range(1,7):
    if i>1:
        url='https://www.qiushibaike.com/text/page/'+str(i)+'/'
    r=requests.get(url)
    demo = r.text
    soup = BeautifulSoup(demo,"html.parser")
    soup.prettify()
    space = [s.extract() for s in soup('br')]
    s=str(soup.find_all('div', class_="content")).replace('\n', '').replace('\r', '')
    m = re.findall(re.compile('<span>(.*?)</span>'),s)    
    with open(filename,'a',encoding='utf-8') as f:
        for joke in m:
            print(joke,file=f)


    
    
