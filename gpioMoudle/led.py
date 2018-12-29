#!/usr/bin/python
# -*- coding: UTF-8 -*-  
# RaspberryGPIO - led.py
# 2018/12/14 9:00
# Author:Kencin <myzincx@gmail.com>
"""
设备：红绿黄三色小灯
功能：传入三个不同颜色LED灯的引脚，进行单个点亮或者跑马灯
"""


import RPi.GPIO as GPIO
import time


class LedLight(object):
    red = 0
    green = 0
    yellow = 0

    def __init__(self, pin_red, pin_green, pin_yellow):
        self.red = pin_red
        self.green = pin_green
        self.yellow = pin_yellow
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.red, GPIO.OUT)
        GPIO.setup(self.yellow, GPIO.OUT)
        GPIO.setup(self.green, GPIO.OUT)

    # 跑马灯
    def run_led(self):
        while num > 0:
            GPIO.output(self.red, 1)
            time.sleep(0.5)
            GPIO.output(self.red, 0)
            GPIO.output(self.yellow, 1)
            time.sleep(0.5)
            GPIO.output(self.yellow, 0)
            GPIO.output(self.green, 1)
            time.sleep(0.5)
            GPIO.output(self.green, 0)
            num = num - 1

    # 单个控制模块
    def control_red(self, flag):
        GPIO.output(self.red, flag)

    def control_yellow(self, flag):
        GPIO.output(self.yellow, flag)

    def control_green(self, flag):
        GPIO.output(self.green, flag)
