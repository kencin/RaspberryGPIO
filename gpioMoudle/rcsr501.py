#!/usr/bin/python
# -*- coding: UTF-8 -*-  
# RaspberryGPIO - rcsr501.py
# 2018/12/14 17:18
# Author:Kencin <myzincx@gmail.com>

import RPi.GPIO as GPIO


class Rcsr501():
    rcsr_pin = 0

    def __init__(self, pin):
        self.rcsr_pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.rcsr_pin, GPIO.IN)

    def check_body(self):
        return GPIO.input(self.rcsr_pin)
