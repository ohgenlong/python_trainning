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

# 对sequence中的item依次执行function(item)，见执行结果组成一个List返回

def cube(x): return x*x*x
print map(cube, range(1, 11))

def cube(x) : return x + x
print map(cube , "abcde")

def add(x, y): return x+y
print map(add, range(8), range(8))
