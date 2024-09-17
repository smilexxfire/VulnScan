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

from common.module import Module
from common.task import Task
from config.settings import MONGO_COLLECTION
from config.log import logger

class Nuclei(Module, Task):
    def __init__(self, url, severity, task_id):
        self.module = "vulnscan"
        self.source ="nuclei"
        self.collection = MONGO_COLLECTION
        self.target = url
        self.severity = severity
        Module.__init__(self)
        Task.__init__(self, task_id)

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
        self.receive_task()
        self.do_scan()
        self.deal_data()
        self.save_db()
        self.delete_temp()
        self.finish()
        self.finnish_task(self.elapse, len(self.results))

def run(url, severity, task_id):
    nuclei = Nuclei(url, severity, task_id)
    nuclei.run()

if __name__ == '__main__':
    run("http://43.142.109.233:8848/", "critical", "43432,434324,3242")
