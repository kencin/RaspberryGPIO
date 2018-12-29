#!/usr/bin/python
# -*- coding: UTF-8 -*-  
# RaspberryGPIO - main.py
# 2018/12/14 17:00
# Author:Kencin <myzincx@gmail.com>

from gpioMoudle import led
from gpioMoudle import rcsr501 as rcsr
import json
import time
import MQTT.control
import gpioMoudle.dht11
import copy
from AliyunIOT import  aliIOT
import multiprocessing
from gpioMoudle import piCamera
import RPi.GPIO as GPIO
import QiNiuOSS.fileUpload as qiniu

# BCM引脚 red:14 green:18 yellow:15
# led = led.LedLight(14, 18, 15)
# BCM引脚 rcsr:12
# rcsr = rcsr.Rcsr501(12)


# 监测到人亮红灯
# def check_and_light():
#     print(rcsr.check_body())
#     if rcsr.check_body():
#         led.control_red(1)
#     else:
#         led.control_red(0)
#     time.sleep(1)


if __name__ == '__main__':
    """
    iot = aliIOT.AliIot()
    iot.on_connect = on_connect
    iot.on_message = on_message
    q = multiprocessing.Process(target=iot.connect(send_data))
    q.start()
    """
    # pi_camera = piCamera.ThePiCamera()
    # pi_camera.take_photo()
    control = MQTT.control.Control()
    control.connect()

    # dht = gpioMoudle.dht11.DHT11(23)
    # dht2 = copy.deepcopy(dht)
    # t, h = dht.get_dht()
    # print(dht2.get_dht())

    # dirs = '/home/kencin/Desktop/image.jpg'
    # q = qiniu.FileUpload('image.jpg', dirs)
    # q.upload()


