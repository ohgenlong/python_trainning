#!/usr/bin/env python
# -*- coding=UTF-8 -*-
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


from multiprocessing import Process,Pipe,Queue

## 多进程队列
## 作用：父进程和子进程之间交互数据，子进程put，父进程get


def run(q):
    for i in range(20):
        q.put("queue parma:%s" % i)

if __name__=="__main__":
    queue = Queue()
    p = Process(target=run,args=(queue,))
    p.start()

    ## print parent_conn.recv() 如果这里多加了一个recv的方法，就不会看到下面的队列的输出，会一直卡在这里
    while True:
        if not queue.empty():
            value = queue.get()
            print  value
    p.join()
