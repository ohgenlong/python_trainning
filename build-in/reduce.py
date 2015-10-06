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
# 对sequence中的item顺序迭代调用function，如果有starting_value，还可以作为初始值调用，例如可以用来对List求和
print reduce(lambda x,y:x+y, range(100))

def add(x,y): return x + y
print reduce(add ,range(1,100))
print reduce(add, range(1,11))
print reduce(add, range(1,11), 20)
print range(1,11)