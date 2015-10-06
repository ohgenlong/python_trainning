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
            data = data.split("|")
            if hasattr(self,data[0]):
                func = getattr(self,data[0])
                func(data[1:])
            else:
                print "No module found!"

    def file_transfer(self,msg):
        print "Recv-->%s" % msg
        if msg[0] == "get":
            #print "--> Going to send file: %s to client" % msg[1]
            get_file_name = msg[1]
            if os.path.isfile(get_file_name):
                file_size = os.path.getsize(get_file_name)
                print "Send-->file_transfer|%s|get|ready|%s" % (get_file_name,file_size)
                self.request.send("file_transfer|%s|get|ready|%s" % (get_file_name,file_size))
                client_ack = self.request.recv(1024)
                if client_ack.startswith("file_transfer|%s|get|recv|ready" % get_file_name):
                    print "Recv-->%s" % client_ack
                    f = file(get_file_name,"rb")
                    for i in f:
                        self.request.send(i)
                    else:
                        print "Send-->file %s transfer done!" % get_file_name
                        #self.request.send("file %s transfer done!" % get_file_name)
                        f.close()
                else:
                    print "Send-->client is not ready,please reconnect..."
            else:
                print "Send-->file %s is not found!" % get_file_name
                self.request.send("file %s is not found!" % get_file_name)
        else:
            print "Send-->No action found!"
            self.request.send("No action found!")

if __name__ == "__main__":
    HOST,PORT = "0.0.0.0",9999
    server = SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()