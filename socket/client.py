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

import socket

HOST = "192.168.31.126"
PORT = 9999
tcpClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpClient.connect((HOST,PORT))
BUFSIZE=8096

while True:
    data_send = raw_input(">> ").strip()
    if not data_send:continue
    tcpClient.sendall(data_send)
    data_recv = tcpClient.recv(BUFSIZE)
    if not data_recv:continue
    print data_recv.strip()

tcpClient.close()

