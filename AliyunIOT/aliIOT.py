#!/usr/bin/python
# -*- coding: UTF-8 -*-  
# RaspberryGPIO - aliIOT.py
# 2018/12/14 19:57
# Author:Kencin <myzincx@gmail.com>

import AliyunIOT.config as config
import json
import aliyunsdkiotclient.AliyunIotMqttClient as iot
import multiprocessing

HOST = config.IOT['PRODUCE_KEY'] + '.iot-as-mqtt.cn-shanghai.aliyuncs.com'
SUBSCRIBE_TOPIC = "/" + config.IOT['PRODUCE_KEY'] + "/" + config.IOT['DEVICE_NAME'] + "/control"


class AliIot(object):

    def __init__(self):
        print("连接阿里云IOT初始化中...")

    def on_connect(self, client, userdata, flags, rc):
        print("请重构on_connect函数")
        client.subscribe(topic=SUBSCRIBE_TOPIC)

    def on_message(self, client, userdata, msg):
        print("请重构on_message函数")
        print('receive message topic :' + msg.topic)
        print(str(msg.payload))

    def worker(self, client, send_data):
        topic = '/sys/' + config.IOT['PRODUCE_KEY'] + '/' + config.IOT['DEVICE_NAME'] + '/thing/event/property/post'
        payload_json = send_data()
        print('send data to iot server: ' + str(payload_json))
        client.publish(topic, payload=str("payload_json"))

    def connect(self, send_data):
        client = iot.getAliyunIotMqttClient(config.IOT['PRODUCE_KEY'], config.IOT['DEVICE_NAME'],
                                            config.IOT['DEVICE_SECRET'], secure_mode=3)
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(host=HOST, port=1883, keepalive=60)
        p = multiprocessing.Process(target=self.worker, args=(client, send_data))
        p.start()
        client.loop_forever()




