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

## 多进程之间共享数据
## 多进程互相之间的内存资源（变量）不共享，只有通过中介控制来接收各进程传过来的值进行处理这一个方法达到共享的效果

def run(num,lock,share_list,share_dict,n):
#def run(num,share_list,share_dict,n):
    time.sleep(0.5)
    lock.acquire()  ## 获取进程锁
    print "I am doing add list: %s" % num
    share_list.append(num)
    share_dict[num] = num
    n += 1
    print "run n :",n
    lock.release()  ## 释放进程锁

if __name__ == "__main__":
    n = 0
    m = multiprocessing.Manager()  ## 进程之间交互的中介
    s_list = m.list()
    s_dict = m.dict()
    l = multiprocessing.Lock()  ## 进程之间的锁，用法主要在进城之间打印时比较整齐
    p_list = []
    for i in range(20):
        p = multiprocessing.Process(target=run,args=(i,l,s_list,s_dict,n,))
        #p = multiprocessing.Process(target=run,args=(i,s_list,s_dict,n,))
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()

    time.sleep(2)
    print "share_list:",s_list,"len:",len(s_list)
    print "share_dict:",s_dict
    print "n:",n  ## 这里的n和run函数里面的n不是同一个n，虽然名字一样，虽然传递进run函数，但是run函数会自己复制一份作为己用
                  ## 所以这里打印的还是原来的值：0