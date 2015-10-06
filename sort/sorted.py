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
from operator import itemgetter, attrgetter

def f(x):
    return x**2

g = lambda x:x**2

j = map(lambda x:x**2 ,range(1,10))

print type(j)
print j

sorted(j)

student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10)]
print "1:",sorted(student_tuples, key=itemgetter(2))  ## 按第三个元素排序
print "2:",sorted(student_tuples, key=itemgetter(1,2)) ## 先按第二个元素，如相同，再按第三个元素排序
print "3:",sorted(student_tuples, key=itemgetter(2), reverse=True) ## 按第三个元素倒序

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [Student('john', 'A', 15),Student('jane', 'B', 12),Student('dave', 'B', 10)]
print "4:",sorted(student_objects, key=attrgetter('age')) ## 按类Student()里面的年龄排序
print "5:",sorted(student_objects, key=lambda student: student.age) ## 同上
print "6:",sorted(student_tuples, key=lambda student: student[2]) ## 效果同上。不同的是上面的例子用属性，这个用下标
print "7:",sorted(student_objects, key=attrgetter('grade', 'age')) ## 先按类Student()里面的年级排序，如相同，在按类Student()里面的年龄排序
print "8:",sorted(student_objects, key=attrgetter('age'), reverse=True) ## 按类Student()里面的年龄倒序
## 先按年龄排序，再按成绩排序
s=sorted(student_objects,key=attrgetter('age'))
print "9:",sorted(s,key=attrgetter('grade'),reverse=True)

## 按第一个元素排序，如果第一个元素相同，保持之前的先后顺序
data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print "10:",sorted(data, key=itemgetter(0))

## 结果
## 1: [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
## 2: [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
## 3: [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
## 4: [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
## 5: [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
## 6: [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
## 7: [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
## 8: [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
## 9: [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
## 10: [('blue', 1), ('blue', 2), ('red', 1), ('red', 2)]


