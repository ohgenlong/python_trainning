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

def calc(n):
    print "-->",n
    if n/2 > 0:
        return calc(n/2)
    print "---"
    return n

print  calc(12)

a = range(100)


