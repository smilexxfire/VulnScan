# -*- coding: UTF-8 -*-
'''
@Project ：VulnScan 
@File    ：producer.py
@IDE     ：PyCharm 
@Author  ：smilexxfire
@Email   : xxf.world@gmail.com
@Date    ：2024/9/12 13:37 
@Comment ： 
'''
import json

from common.database.producer import RabbitMQProducer
from config.settings import RABBITMQ_QUEUE_NAME

def purge_queue():
    """
    清空队列

    :param queue_name: 队列名称
    :return:
    """
    producer = RabbitMQProducer(RABBITMQ_QUEUE_NAME)
    producer.purge_queue()

def send_task(task):
    producer = RabbitMQProducer(RABBITMQ_QUEUE_NAME)
    producer.publish_message(json.dumps(task))

if __name__ == '__main__':
    task = {
        "url": "http://43.142.109.233:8848/",
        "severity": "critical"
    }
    send_task(task)
