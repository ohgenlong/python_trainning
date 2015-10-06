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

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        print '''
        <-->info of %s<-->
              name: %s
              age: %s
              sex: %s''' % (self.name,self.name,self.age,self.sex)

class School(object):
    def __init__(self,sch_name,addr,tel):
        self.sch_name = sch_name
        self.addr = addr
        self.tel = tel
        self.stu_list = []
        self.t_list = []


class Student(SchoolMember,School):  ## 多继承
    def __init__(self,name,age,sex,grade):
        SchoolMember.__init__(self,name,age,sex)
        School.__init__(self,"Bj university","Bj","110")
        self.grade = grade
    def pay_money(self):
        print "--> %s is free" % self.name
    def tell(self):  ## 重写父类的函数
        SchoolMember.tell(self)  ## 调用父类的函数
        print """
        ---> from grade %s
        ---> from sclool %s
                  addr %s """ % (self.grade,self.sch_name,self.addr)


class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary):
        SchoolMember.__init__(self,name,age,sex)
        self.salary = salary

s = Student("john","21","male","2")
s.tell()  ## 改写父类的tell()函数
print s.grade


s = Student("Kate",'22','female',"3")
s.tell()
print s.grade


t = Teacher("Make",'30','male','50000')
t.tell()
print t.salary