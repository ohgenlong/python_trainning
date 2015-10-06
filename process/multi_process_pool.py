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

import multiprocessing

## 进程池实例
## 控制同时有多少个进程在运行

#def run(num,lock,share_list):
def run(num,share_list):
    time.sleep(1)
    #lock.acquire()
    share_list.append(num)
    print "Add %s to share_list" % num
    #lock.release()
    return share_list

if __name__=="__main__":
    l = multiprocessing.Lock()

    pool = multiprocessing.Pool(processes=5) ## 控制最多同时有5个进程在运行，设置成CPU的核数一样多就ok

    ## 创建多进程的中介处理实例
    m = multiprocessing.Manager()
    s_list = m.list()

    p_list = []
    for i in range(20):
        #p = pool.apply_async(run,args=(i,l,s_list,))
        p = pool.apply_async(run,args=(i,s_list,)) ## 把run函数放到进程池
        p_list.append(p) ## 启动进程池，并且加入p_list让多进程并发

    for p in p_list:
        print p.get() ## 跟p.join()效果一样，取进程的结果

    print "share_list:",s_list


