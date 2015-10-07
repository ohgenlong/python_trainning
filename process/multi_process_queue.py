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

import multiprocessing
from multiprocessing import Process,Queue,Pool
import os, time, random

## 多进程队列
## 作用：父进程和子进程之间交互数据，子进程put，父进程或者另外子进程get


# 写数据进程执行的代码:
def write_em1(q):
    for v in ['A','B','C']:
        print 'Put %s to queue...' % v
        q.put(v)
        time.sleep(random.random())

# 写数据进程执行的代码:
def write(n,q,l):
    #for num in range(n):
    l.acquire()
    print 'Put %s to queue...' % n
    q.put(n)
    time.sleep(0.5)
    l.release()

# 读数据进程执行的代码:
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print 'Get %s from queue.' % value
            time.sleep(random.random())
        else:
            break # pr进程里是死循环，无法等待其结束，只能当队列为空时强行终止


if __name__=='__main__':
    ## 没用进程池的调用例子
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    l = multiprocessing.Lock()
    p_list_em1 = []

    # 同时创建20个写入子进程
    for i in range(20):
        pw = Process(target=write, args=(i,q,l,))
        # 启动子进程pw，写入:
        pw.start()
        # 将子进程放进列表，控制是否等待子进程结束后返回才让主进程退出
        p_list_em1.append(pw)

    for p in p_list_em1:
        # 等待pw结束:
        p.join()

    ## 创建读取子进程
    pr = Process(target=read, args=(q,))
    # 启动子进程pr，读取:
    pr.start()
    ## 等待pr结束：
    pr.join()
    print
    print "all data write and read done"
    print
    print "Process Pool example...\n"
    ## 注意：队列对象不能在父进程与子进程间通信，如果想要使用进程池中使用队列则要使用multiprocess的Manager类，如下：
    manager = multiprocessing.Manager()
    # 父进程创建Queue，并传给各个子进程：
    q = manager.Queue()
    lock = manager.Lock() ## 创建队列锁，保证同一时间，只有一个进程在对队列进行操作
    p = Pool(processes=5) ## 保证每次只能5个进程在同时运行
    p_list = []
    # 同时开20个进程
    for i in range(20):
        pw = p.apply_async(write,args=(i,q,lock))
        p_list.append(pw)
    for p in p_list:
        p.get()

    p = Pool()
    time.sleep(0.5)
    pr = p.apply_async(read,args=(q,))
    p.close() # 调用get()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    p.join()


    print
    print 'all data write and read done'
