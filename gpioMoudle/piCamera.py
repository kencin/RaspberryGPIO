#!/usr/bin/python
# -*- coding: UTF-8 -*-  
# RaspberryGPIO - piCamera.py
# 2018/12/15 10:19
# Author:Kencin <myzincx@gmail.com>
from picamera import PiCamera
import time


class ThePiCamera(object):
    def __init__(self):
        self.camera = PiCamera()
        # self.camera.resolution = (720, 480)  # 设置照片分辨率
        self.camera.resolution = (2592, 1944)  # 原始分辨率，即500万像素

    def take_photo(self):
        ticks = int(time.time())
        file_name = 'raspi%s.jpg' % ticks
        file_path = '/mnt/hdd/PiPhotos/%s' % file_name
        self.camera.start_preview()  # 预热两秒以获得更清晰的照片
        time.sleep(2)
        self.camera.capture(file_path)
        self.camera.close()
        return file_path, file_name
