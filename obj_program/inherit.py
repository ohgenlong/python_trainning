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

class SchoolMember(object): ## 新式类的定义
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

class School(object): ## 新式类的定义
    def __init__(self,sch_name,addr,tel):
        self.sch_name = sch_name
        self.addr = addr
        self.tel = tel
        self.__stu_list = []  ## 定义私有变量学生列表，不能直接通过外部调用随便删除
        self.__t_list = [] ## 定义私有变量老湿列表，不能直接通过外部调用随便删除

    def return_stu_list(self): ## 定义返回内部变量的函数
        return self.__stu_list

    def add_stu_list(self,cls): ## 定义添加内部变量的函数
        self.__stu_list.append(cls)

    def remove_stu_list(self,cls): ## 定义删除内部变量的函数
        self.__stu_list.remove(cls)

class Student(SchoolMember):
    def __init__(self,name,age,sex,grade,school):  ## 把school类实例作为参数传入
        #SchoolMember.__init__(self,name,age,sex)  ## 旧式类继承写法
        super(Student,self).__init__(name,age,sex) ## 新式类继承写法
        self.school = school ## 调入school类实例后私有化实例
        self.grade = grade
        self.school.add_stu_list(self) ## 把当前类的信息加入school类实例的属性

    def pay_money(self):
        print "--> %s is free" % self.name

    def tell(self):  ## 重写父类的函数
        SchoolMember.tell(self)  ## 调用父类的函数
        print """
        ---> from grade %s
        ---> from sclool %s
                  addr %s """ % (self.grade,self.school.sch_name,self.school.addr) ## 调用私有化后的school类实例属性

    def transfer(self): ##  删除学生自己的所有信息
        self.school.remove_stu_list(self)

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,school):
        SchoolMember.__init__(self,name,age,sex)  ## 旧式类继承写法
        self.school = school
        self.salary = salary

    def tell(self):  ## 重写父类的函数
        SchoolMember.tell(self)  ## 调用父类的函数
        print """
        ---> from salary %s
        ---> from sclool %s
                  addr %s """ % (self.salary,self.school.sch_name,self.school.addr)

s1 = School("Bj university","BJ","110")
s2 = School("QingHua university","BJ","111")

s11 = Student("john","21","male","2",s1)
s11.tell()  ## 改写父类的tell()函数

s22 = Student("Kate",'22','female',"3",s2)
s22.tell()

s33 = Student("KK",'20','female',"4",s1)
s33.tell()

t = Teacher("Make",'30','male','50000',s1)
t.tell()
print t.salary

for i in s1.return_stu_list():  ## i 就是Student实例，通过调用返回内部变量函数（return_stu_list）来得到内部变量（__stu_list）
    print i.name,id(i)

print

s33.transfer() ## 删除s33这个实例的学生具体信息
for i in s1.return_stu_list():
    print i.name,id(i)

