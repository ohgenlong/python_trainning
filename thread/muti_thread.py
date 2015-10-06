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
    #print "Hi, I am thread %s ..." % num
    global NUM
    #NUM += 1
    lock.acquire()
    #time.sleep(1)
    #lock.acquire()
    print "Hi, I am thread %s ..." % num
    NUM += 1
    lock.release()

NUM = 1
p_list = []
lock = threading.Lock()  ## 加上共享资源NUM的锁，保证NUM同时只被一个线程调用

print "Begin-->",NUM
for i in range(10):
    t = threading.Thread(target=run,args=(i,))
    t.start()  ## 启动主线程，启动多个线程
    p_list.append(t)  ## 将启动的实例放到进程列表，并发执行，但是也要等所有线程执行后统一打印NUM
    #t.join()   ## 启动这个join线程来阻塞主线程

for j in p_list:
    j.join()  ## 启动这个join线程阻塞主线程，等待每一个线程实例结束才能结束

print "End--->",NUM ## 等所有线程执行后统一打印NUM