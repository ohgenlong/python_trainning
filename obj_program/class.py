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

class People(object):
    info = "abc"  ##定义类变量
    def __init__(self,name,age,job):
        self.name = name ## 定义实例变量
        self.__age = age ## 定义实例内部变量
        self.job = job ## 定义实例变量


    @staticmethod  ## 静态方法，不能调用类变量和实例变量
    def static_method():
        print "i am a static_method"

    def walk(self):
        print "%s is walking" % self.name
        print "%s is %s years old" % (self.name,self.__age)
        print "%s is a %s" % (self.name,self.job)

    def talk(self):
        print "%s is talking" % self.name   ## 直接调用 name = 'abc',没有用self.name覆盖掉
        print "%s is %s years old" % (self.name,self.__age)
        print "%s is a %s" % (self.name,self.job)
        print "%s is a test" % People.info
        self.__breath()  ## 私有方法，只能类内部的函数之间调用

    def __breath(self): ## 私有方法，只能类内部的函数之间调用
        print "%s is breathing..." % self.name

    def get_info(self,info_type):  ## 只能查看，利用函数来查看不能修改的内部变量
        if info_type == 'age':
            return self.__age  ##不能修改的内部变量
        elif info_type == 'job':
            return self.job

    def __del__(self):
        print "i am a end..."

a = People("jane",'19','teacher')
a.static_method()
a.walk()
a.talk()

print

b = People("Make",'24','engineer')
b.walk()
b.talk()

print

c = People("Kate",'21','doctor')
c.walk()
c.talk()
print c.get_info('age'),c._People__age
print


a.info = 'a' ## 改变a实例的类变量
print a.info ## 打印类变量
People.info = 'Kity'  ## 改变类变量
print b.info ## 打印类变量
print c.info ## 打印类变量

## 结果
#i am a static_method
#jane is walking
#jane is 19 years old
#jane is a teacher
#jane is talking
#jane is 19 years old
#jane is a teacher
#abc is a test
#jane is breathing...
#
#Make is walking
#Make is 24 years old
#Make is a engineer
#Make is talking
#Make is 24 years old
#Make is a engineer
#abc is a test
#Make is breathing...
#
#Kate is walking
#Kate is 21 years old
#Kate is a doctor
#Kate is talking
#Kate is 21 years old
#Kate is a doctor
#abc is a test
#Kate is breathing...
#21 21
#
#a
#Kity#
#Kity
#i am a end...
#i am a end...
#i am a end...