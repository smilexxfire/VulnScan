# -*- coding: UTF-8 -*-
'''
@Project ：VulnScan 
@File    ：nuclei.py
@IDE     ：PyCharm 
@Author  ：smilexxfire
@Email   : xxf.world@gmail.com
@Date    ：2024/9/12 12:52 
@Comment ： 
'''
import json
import os
import subprocess
import sys
sys.path.append("D:\\pythonProject\\VulnScan")

from common.module import Module
from config.settings import MONGO_COLLECTION
from config.log import logger

class Nuclei(Module):
    def __init__(self, url, severity):
        self.modules = "vulnscan"
        self.source ="nuclei"
        self.collection = MONGO_COLLECTION
        self.target = url
        self.severity = severity
        Module.__init__(self)

    def do_scan(self):
        cmd = [self.execute_path, "-u", self.target, "-s", self.severity, "-j", "-o", self.result_file]
        subprocess.run(cmd)

    def deal_data(self):
        logger.log("INFOR", "Start deal data process")
        if not os.path.exists(self.result_file):
            return
        with open(self.result_file, "r", encoding="utf8") as f:
            datas = f.readlines()
            for data in datas:
                data = data.strip()
                data = json.loads(data)
                del data["template-path"]
                self.results.append(data)


    def save_db(self):
        # print(self.results)
        super().save_db()

    def run(self):
        self.begin()
        self.do_scan()
        self.deal_data()
        self.save_db()
        self.delete_temp()
        self.finish()

def run(url, severity):
    nuclei = Nuclei(url, severity)
    nuclei.run()

if __name__ == '__main__':
    run("http://43.142.109.233:8848/", "critical")
