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
#1. 有yield关键字的函数则会被识别为generator函数，此时其实函数返回的仍然是iterator。
#2. generator函数用来生成一个序列，但不是一次完成，而是经过多次调用：调用generator函数得到一个generator的对象。
#   之后每次调用generator的next()或__next__()方法都会得到序列的下一个值。
#3. 如何做到的？
# generator的next()或__next__()导致generator函数被调用，遇到yield，返回序列一个值，然后generator函数挂起。
# 下一个next()或__next__()让generator函数恢复，从挂起处往后继续执行。
#
# 这样做的好处之一是不必一次生成序列所有元素（例如序列很长时，存所有元素并不好），而是像有一个iterator一样一个个生成。

def run():
    for i in range(100):
        print "--",i
        yield i

task = run()
task.next()
print "do sth"
task.next()
print "do sth"
task.next()
print "do sth"
task.next()
print "do sth"
task.next()
task.next()