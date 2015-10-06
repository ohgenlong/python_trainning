#!/usr/bin/env python
#-*- coding=UTF-8 -*-
# author: ohgenlong

import os
import sys
import logging
import ConfigParser
import time
import datetime
import json
import traceback
from logging.handlers import RotatingFileHandler

import threading
import random


"""
红灯：event.isSet()为false
绿灯：event.isSet()为true
黄灯：event.isSet()为true
"""

def light():
    if not event.isSet(): ## 判断是否为绿灯，如果是红灯，做下面的
        event.set()  ## set 标志位（转绿灯），set了标志位后event.isSet()为true
    count = 0
    while True:
        if count < 5: ## 如果count小于5，显示绿灯，继续等1秒，累加
            print "\033[42;1mgreen light on\033[0m"
        elif count < 10: ## 如果count大于5，少于10，显示黄灯，继续等1秒，累加
            print "\033[43;1myellow light on\033[0m"
        elif count < 20: ## 如果count大于10，少于20，显示红灯，继续等1秒，累加
            if event.isSet(): ## 检验是否set了标志位（绿灯），然后做下面的
                event.clear() ## 清楚标志位（转红灯）
            print "\33[41;1mred light on\33[0m"
        else: ## 如果count大于20，做下面
            count = 0  ## 重新算count
            event.set()  ## set标志位（转绿灯）
        time.sleep(1)
        count += 1

def car(num):
    while True:
        time.sleep(random.randrange(5)) ## 随机sleep 2秒
        if event.isSet(): ## 如果set了标志位（绿灯）
            print "car %s is running" % num
        else:
            print "car %s is waiting" % num
            event.wait() ## 等待标志位被set（转绿灯）
            print "car %s is running" % num

if __name__ == "__main__":
    event = threading.Event()  ## 建立event实例
    l = threading.Thread(target=light)  ## 把light函数作为线程实例化
    l.start() ## 启动实例化后的线程

    for i in range(1,5):
        c = threading.Thread(target=car,args=(i,)) ## 三个car线程实例化
        c.start() ## 启动实例化后的线程

