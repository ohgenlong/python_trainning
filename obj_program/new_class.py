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

## 旧类继承演示
class a():
    def save(self):
        print "save A"

class b(a):
    pass

class c(a):
    def save(self):
        print "save C"

class d(b,c):  ## 继承左边的，后边的不理，不管他们有没有重写里面的方法
    pass

print u"旧类继承演示"
dd = d()
dd.save()

print

## 新类继承演示
class a(object):
    def save(self):
        print "save A"

class b(a):
    #def save(self):
        #print "save B"
    pass

class c(a):
    def save(self):
        print "save C"
    #pass
class d(c,b): ## 继承有变化的，不继承没有变化的,如果两个都有变化，继承左边的
    pass

print u"新类继承演示"
dd = d()
dd.save()





