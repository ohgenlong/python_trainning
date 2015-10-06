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

import SocketServer


class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        while True:
            ## 客户端发来的数据，然后执行命令
            data = self.request.recv(2048).strip()
            print "{}:write".format(self.client_address[0])
            cmd_res = os.popen(data).read()
            if len(cmd_res) == 0:
                cmd_res = "cmd has no feedback"
            self.request.sendall(cmd_res)

if __name__ == "__main__":
    HOST,PORT = "0.0.0.0",9999
    server = SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()