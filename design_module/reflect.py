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

class myclass():

    def sayhi(self):
        print "sayhi"

    def hang(self):
        print "hang"

def extend():
    print "extend"

m = myclass()

user_input = "aaa"

if hasattr(m,user_input):  ## 判断m这个实例里面有user_input的值的方法
    func = getattr(m,user_input)  ## 从m这个实例里面拿出名字为user_input的值的方法
    func()
else:
    setattr(m,user_input,extend)  ## 复制extend函数到类myclass里面，名字为user_input的值
    f = getattr(m,user_input)
    f()
    m.aaa()
