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



def run1():
    lock.acquire()
    print "run1 plus...."
    global num1
    num1 += 1
    lock.release()
    return num1


def run2():
    lock.acquire()
    print "run2 plus...."
    global num2
    num2 += 1
    lock.release()
    return num2

def run3():

    lock.acquire()
    res1 = run1()
    print "======="
    res2 = run2()
    lock.release()

    print res1,res2


if __name__ == "__main__":
    num1 = num2 = 0
    lock = threading.RLock() ## 递归锁，在多个锁同时进行获取和释放的时候使用，不会因为函数间锁的争用产生问题
    p_list = []
    for i in range(10):
        t = threading.Thread(target=run3)
        t.start()
        p_list.append(t)

    for i in p_list:
        i.join()

