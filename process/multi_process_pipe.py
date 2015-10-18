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


from multiprocessing import Process,Pipe,Queue

## 多进程管道
## 作用：父进程和子进程之间交互数据，像一个队列，子进程send，父进程receive


def f(conn):
    conn.send([42,None,'hello'])
    conn.send("test1")
    conn.send({"t":"test2"})
    conn.close()

if __name__=="__main__":
    parent_conn,child_conn = Pipe()
    p = Process(target=f,args=(child_conn,))
    p.start()

    print parent_conn.recv()
    print parent_conn.recv()
    print parent_conn.recv()
    ## print parent_conn.recv() 如果这里多加了一个recv的方法，就不会看到下面的队列的输出，会一直卡在这里
    p.join()

