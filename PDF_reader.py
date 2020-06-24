# -*- coding: utf-8 -*-
"""
Created on Mon May 18 09:46:35 2020

@author: 81552
"""
import fitz
import json
#"Algorithms, 4th Edition 1.1 Basic Programming Model.pdf"

def text_fix(text):
    text=text.replace("\n"," ").replace("@"," ")
    text = text.replace("."," ").replace(",", " ").replace(':',' ').replace(';',' ').replace("■"," ").replace("!"," ")
    text = text.replace("("," ").replace(")"," ").replace('[',' ').replace(']',' ').replace('"',' ').replace("'"," ")
    text = text.replace('{',' ').replace('}',' ').replace('||'," ")
    text=text.replace("  "," ")
    text = text.replace("<","").replace(">","").replace('-','').replace("-","")
    return text

words_dic={}
print('输入PDF名（仅限英文文件）：')
pdf_document = str(input())
print('输入你想放入的txt文件名：')
file=str(input())+'.txt'
doc = fitz.open(pdf_document)
print ("number of pages: %i" % doc.pageCount)
for p in range(0,doc.pageCount):       
    page = doc.loadPage(p)
    text = text_fix(page.getText("text"))
    words=text.split(' ')
    for word in words:
        if word not in words_dic:
             words_dic[word]=1
        else:
             words_dic[word]+=1
    print('page'+str(p)+'------done')
        
with open(file,'a',encoding='utf-8') as f_obj:
    json.dump(words_dic,f_obj)       
print("JSON数据已经统计好放入"+file+"中")
print('输入0退出应用')
test=input()
while test!=0 :   
    print('输入0退出应用')
    test=int(input())
    
