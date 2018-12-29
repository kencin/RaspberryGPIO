#!/usr/bin/python
# -*- coding: UTF-8 -*-  
# RaspberryGPIO - control.py
# 2018/12/20 22:57
# Author:Kencin <myzincx@gmail.com>

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import MQTT.config as config
import gpioMoudle
import json
import time
import QiNiuOSS.fileUpload as qiniu


class Control(object):
    def __init__(self):
        # print("连接MQTT初始化中...")
        pass

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("raspberry")

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload, encoding="utf-8"))
        if str(msg.payload, encoding="utf-8") == "TurnOnLed":
            led = gpioMoudle.led.LedLight(14, 18, 15)
            led.control_red(1)
        if str(msg.payload, encoding="utf-8") == 'TurnOffLed':
            led = gpioMoudle.led.LedLight(14, 18, 15)
            led.control_red(0)
        if str(msg.payload, encoding="utf-8") == 'getT':
            dht = gpioMoudle.dht11.DHT11(23)
            t, h = dht.get_dht()
            while t == -100:
                time.sleep(1)
                t, h = dht.get_dht()
            # print(t)
            data = {
                "T": t,
                "H": h
            }
            print(str(data))
            publish.single("T_H", payload=str(data), hostname=config.HOST,
                            auth={'username': config.MQTT_USERNAME, 'password': config.MQTT_PASSWORD})
        if str(msg.payload, encoding="utf-8") == 'tkphoto':
            tkphoto = gpioMoudle.piCamera.ThePiCamera()
            path, name = tkphoto.take_photo()
            q = qiniu.FileUpload(name, path)
            q.upload()
            photo_url = q.file_url + name
            publish.single("photo", payload=photo_url, hostname=config.HOST,
                           auth={'username': config.MQTT_USERNAME, 'password': config.MQTT_PASSWORD})

    def connect(self):
        client = mqtt.Client(client_id="", clean_session=True, userdata=None, transport="tcp")
        client.username_pw_set(config.MQTT_USERNAME, password=config.MQTT_PASSWORD)
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(config.HOST, 1883, 60)
        client.loop_forever()
