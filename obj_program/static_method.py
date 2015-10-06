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

class MyClass():
    age = '22'
    def __init__(self):
        self.name = 'kate'

    def sayhi1(self):
        print "sayhi normal"

    @staticmethod
    def sayhi2():
        print "i am a static method"

    @classmethod ## 不需要实例化立刻调用,但是不能调用实例变量,可以调用类变量
    def sayhi3(self):
        print "i am a class method"
        print self.age ## 调用类变量
        #print self.name ## 调用实例变量

    @property ## 把一个函数变成一个静态属性，例如self.age,self.name,就不用执行，可以用属性的调用方法来获取到该值
    def sayhi4(self):
        print "i am a property"
        return "property"

cls = MyClass()
cls.sayhi1()
cls.sayhi2()
MyClass.sayhi3()
print cls.sayhi4



