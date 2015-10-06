#!/usr/bin/env python
# -*- coding=UTF-8 -*-
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

import paramiko

host = sys.argv[1]
user = 'root'
password = 'qwe123'
cmd = sys.argv[2]

s = paramiko.SSHClient()  ## 绑定实例
s.load_system_host_keys()  ## 加载本机knows_host主机文件
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  ## 省去第一次登陆时的交互

s.connect(host, 22, user, password, timeout=5)
stdin, stdout, stderr = s.exec_command(cmd)

cmd_result = stdout.read(), stderr.read()

for line in cmd_result:
    print line,

s.close()
