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
    global a
    if not num == 6:
        print "<-->"
    time.sleep(2)
    print num
    a.append(num)



def main(n):
    print "-->> begin thread main"
    for i in range(n):
        t = threading.Thread(target=run,args=(i,)) ## 主线程main再开多个子线程
        t.start()
    time.sleep(2)
    print "-->> end"

if __name__ == "__main__":
    a = []
    abc = threading.Thread(target=main,args=(10,))  ## 启动主线程main
    ## 守护进程，如果主线程执行完以后,
    ## 还有其他非守护线程,主线程是不会退出的，会被无限挂起；
    ## 必须将线程声明为守护线程之后，如果主线程队列中的数据运行完了，那么整个程序想什么时候退出就退出，不用等待
    abc.setDaemon(True)
    abc.start()

    print ">>>>>"
    time.sleep(1.5)
    print a

