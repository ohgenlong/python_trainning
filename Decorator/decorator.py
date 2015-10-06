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
import functools


print u"多个装饰器放在一个装饰器中串行进行执行"
## 多个装饰器放在一个装饰器中串行进行执行
def default(func):
    def run(args):
        a = auth(func)  ## 装饰器1
        b = auth2(func) ## 装饰器2
        return a(args),b(args)  ## 被封装函数t1()中有返回值，故这里用return
    return run

## 装饰器1
def auth(func):
    def aa(args):  ## 因被封装函数t1()有参数
        print "welcome !!"
        func(args) ## 这里是传t1()的参数进来，然后再调用t1(),但是不返回
    return aa

## 装饰器2
def auth2(func):
    def acl(args):
        print "pass correct!"
        return func(args)  ## 这里是传t1()的参数进来，然后再调用t1(),返回值
    return acl

@default  ## 等价于 t1 = default(t1)
def t1(args):
    print "t1"
    return args

print t1('abc')

print "<========================================>"

print u"多个装饰器嵌套"
#多个装饰器嵌套
def decorator1(func):
    def _run():
        print "----->"
        func()

    return _run

def decorator2(func):
    def _run():
        print "=====>"
        func()

    return _run

@decorator1
@decorator2
def runner():
    print "i am the runner..."

runner()

print "<=========================================>"

print u"把被封装函数(foo())的__name__、__module__、__doc__和 __dict__都复制到封装函数(wrapper())去"
## 把被封装函数(foo())的__name__、__module__、__doc__和 __dict__都复制到封装函数(wrapper())去
def timeit(func):
    @functools.wraps(func)  ## 如果没有这个，最后foo.__name__的结果是wrapper而不是foo
    def wrapper():
        start = time.clock()
        print "start:",start
        func()
        end =time.clock()
        print "end:",end
        print 'used:', end - start
    return wrapper

@timeit
def foo():
    "i am the foo doc"
    print 'in foo()'

foo()

print foo.__name__
print foo.__module__
print foo.__doc__
print foo.__dict__

print "<=========================================>"

print u"被封装的函数带参数"
## 被封装的函数带参数
def deco(func):
    def _deco(*args, **kwargs):
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("  after %s called. result: %s" % (func.__name__, ret))
        return ret
    return _deco

@deco
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a+b

@deco
def myfunc2(a, b, c):
    print(" myfunc2(%s,%s,%s) called." % (a, b, c))
    return a+b+c

myfunc(1, 2)
myfunc(3, 4)
myfunc2(1, 2, 3)
myfunc2(3, 4, 5)