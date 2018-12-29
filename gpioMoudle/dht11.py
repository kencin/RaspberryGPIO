#!/usr/bin/python
# -*- coding: UTF-8 -*-  
# RaspberryGPIO - dht11.py
# 2018/12/15 10:14
# Author:Kencin <myzincx@gmail.com>

# 温湿度传感器 DHT11
import RPi.GPIO as GPIO
import time


class DHT11(object):
    dht_pin = 0

    def __init__(self, dht_pin):
        self.dht_pin = dht_pin
        GPIO.setmode(GPIO.BCM)

    def get_dht(self):
        # DHT11 变量
        data = []  # 数据存储
        j = 0

        time.sleep(1)
        # 置为输出，主机发送开始信号，
        GPIO.setup(self.dht_pin, GPIO.OUT)
        GPIO.output(self.dht_pin, GPIO.LOW)
        time.sleep(0.02)  # 主机把总线拉低必须大于18毫秒,保证DHT11能检测到起始信号。
        GPIO.output(self.dht_pin, GPIO.HIGH)

        '''
        置为输入，等待DHT11响应。 本来需要延时等待20-40us后,再读取DHT11的响应信号，
        但是更改模式需要50us,所以不需要延时
        '''
        GPIO.setup(self.dht_pin, GPIO.IN)

        # 等待一个低电平和一个高电平过后才是数据'0'或'1'
        while GPIO.input(self.dht_pin) == GPIO.LOW:
            continue
        while GPIO.input(self.dht_pin) == GPIO.HIGH:
            continue

        '''
        读取40个数据位
        这段代码参考自网上， 主体思路是 首先接收到一个低电平（0，1低电平时延都为50us），
        后因为高电平时延长度（0为26-28us，1为70us），则可以根据k值判断是0还是1
        '''
        while j < 40:
            k = 0
            while GPIO.input(self.dht_pin) == GPIO.LOW:
                continue
            while GPIO.input(self.dht_pin) == GPIO.HIGH:
                k += 1
                if k > 100:
                    break
            if k < 8:
                data.append(0)
            else:
                data.append(1)
            j += 1

        # 数据位赋值
        humidity_bit = data[0:8]
        humidity_point_bit = data[8:16]
        temperature_bit = data[16:24]
        temperature_point_bit = data[24:32]
        check_bit = data[32:40]

        humidity = 0
        humidity_point = 0
        temperature = 0
        temperature_point = 0
        check = 0

        # 2进制 TO 10进制
        for i in range(8):
            humidity += humidity_bit[i] * 2 ** (7 - i)
            humidity_point += humidity_point_bit[i] * 2 ** (7 - i)
            temperature += temperature_bit[i] * 2 ** (7 - i)
            temperature_point += temperature_point_bit[i] * 2 ** (7 - i)
            check += check_bit[i] * 2 ** (7 - i)

        # 校验位
        tmp = humidity + humidity_point + temperature + temperature_point

        # 加上小数点
        temperature += float(temperature_point) / 10

        # 返回值
        if check == tmp:
            return temperature, humidity
        else:
            print("wrong")
            return -100, -100


