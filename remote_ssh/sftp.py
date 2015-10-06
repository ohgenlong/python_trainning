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

import paramiko

host = '192.168.31.126'
port = 22
user = 'root'
password = 'qwe123'

i = paramiko.Transport((host,port))

i.connect(username=user,password=password)

sftp = paramiko.SFTPClient.from_transport(i)

sftp.get('a.py','b.py')
sftp.put('b.py','a.py')



