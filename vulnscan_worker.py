# -*- coding: UTF-8 -*-
'''
@Project ：VulnScan 
@File    ：vulnscan_worker.py
@IDE     ：PyCharm 
@Author  ：smilexxfire
@Email   : xxf.world@gmail.com
@Date    ：2024/9/12 13:32 
@Comment ： 
'''
import json
from common.database.consumer import RabbitMQConsumer
from modules.vulnscan import nuclei
from config.settings import RABBITMQ_QUEUE_NAME

class VulnScanWorker(RabbitMQConsumer):
    def __init__(self, queue_name):
        super().__init__(queue_name)

    def task_handle(self):
        task = json.loads(self.message)
        nuclei.run(task["url"], task["severity"])

if __name__ == '__main__':
    # 监听任务队列
    worker = VulnScanWorker(RABBITMQ_QUEUE_NAME)
    worker.start_consuming()