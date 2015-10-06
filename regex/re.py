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

import re

## match 从文件开头开始匹配
a = "sdfjklgn1234kg*12+_()   (* () 123425fjsdk1234jg12389g71"
print "str:",a
print "match:",re.match("[a-zA-Z]+",a).group()
print "search:",re.search("[^a-zA-Z]+",a).group()
print "findall:",re.findall("[^a-zA-Z]+",a)
print "sub:",re.sub(r'\s+', '-', a, count=2)
print "split:",re.split("[a-zA-Z]+",a)

b = "10.12.13.14"
print "ip:",b
print re.search('(?P<first>\d+).(?P<second>\d+).',b).groupdict()
