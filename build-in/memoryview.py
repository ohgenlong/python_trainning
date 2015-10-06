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

## 本函数是返回对象obj的内存查看对象。所谓内存查看对象，就是对象符合缓冲区协议的对象，为了给别的代码使用缓冲区里的数据，而不必拷贝，就可以直接使用
v = memoryview(b'abc123')
print (v[1])
print (v[0])

import struct
buf = struct.pack("i"*12, *list(range(12)))
x = memoryview(buf)
y = x.cast('i', shape=[2,2,3])
print(y.tolist())