# -*- coding: UTF-8 -*-
'''
@Project ：VulnScan 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：smilexxfire
@Email   : xxf.world@gmail.com
@Date    ：2024/9/12 13:24 
@Comment ： 
'''
import json

with open("1.json","r", encoding="utf8") as f:
    datas = f.readlines()
    for data in datas:
        data = data.strip()
        print(json.loads(data))