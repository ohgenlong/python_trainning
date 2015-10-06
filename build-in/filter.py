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

a = range(10)

## (item)，将执行结果为True的item组成一个List/String/Tuple（取决于sequence的类型）返回
print filter(lambda x:x*x , a)

print globals()

print locals()