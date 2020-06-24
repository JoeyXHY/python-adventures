# -*- coding: utf-8 -*-
"""
Created on Wed May 13 08:00:24 2020

@author: 81552
"""

#高阶函数排序
date=['05-13','05-14','05-15','05-16','05-17']
a=[24,23,19,20,23]
li=list(zip(date,a))
print(sorted(li, key=lambda y:y[1]))
dic=dict(zip(date,a))
print('小于等于20度的日期及其温度')
print(list(filter(lambda x: x[1] <= 20, dic.items())))


def linestring(date,a):
    k=max(a)
    while(k>=min(a)):
        for i in range(0,5):
            if a[i]>=k:
                print(' ■■■■    ',end='')
            elif a[i]<k:
                print('         ',end='')
        print('')
        k-=1
    for j in range(0,5):
            print(' ■■■■    '*5)
    print('——'*22)
    for e in range():
            print(date)
linestring(date,a)

