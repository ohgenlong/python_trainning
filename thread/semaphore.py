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

def run(num):

    semaphore.acquire()
    time.sleep(0.5)
    global NUM
    NUM += 1
    print "Hi, I am thread %s ..." % num
    semaphore.release()

NUM = 0
p_list = []
semaphore = threading.BoundedSemaphore(5)  ## 信号量（也是通过锁来完成），同时可以让多少个线程共用一个共享内存

print "Begin-->",NUM
for i in range(100):
    t = threading.Thread(target=run,args=(i,))
    t.start()  ## 启动主线程，启动多个线程
    p_list.append(t)  ## 将启动的实例放到进程列表，并发执行，但是也要等所有线程执行后统一打印NUM

for j in p_list:
    j.join()  ## 启动这个join线程阻塞主线程，等待每一个线程实例结束才能结束

print "End--->",NUM,len(p_list) ## 等所有线程执行后统一打印NUM