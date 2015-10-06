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

class MyFTP(object):
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def put(self,msg): ## 上传文件
        print "put -->",msg

    def get(self,msg): ## 下载文件
        print "--> get",msg
        if len(msg) > 0:
            remote_filename = msg[0]
            cmd_msg = "file_transfer|get|%s" % remote_filename
            self.tcpClient.send(cmd_msg)
            feedback = self.tcpClient.recv(8096)
            print "filename:",remote_filename
            if feedback.startswith("file_transfer|%s|get|ready" % remote_filename):
                ack_msg = "file_transfer|%s|get|recv|ready" % remote_filename
                self.tcpClient.send(ack_msg)
                file_size = feedback.split("|")[4]
                recv_size = 0
                f = file("recv/%s" % remote_filename,"wb")
                ## 循环接收数据
                while not int(file_size) == recv_size:
                    print file_size,recv_size
                    if int(file_size) - recv_size >= 1024:
                        data = self.tcpClient.recv(1024) ## 每次最大1024个字节，超过的话等待下次再接收
                        recv_size += len(data) ## 接收到的数据长度叠加到已收到的数据变量中
                    else:
                        data = self.tcpClient.recv(int(file_size) - recv_size)
                        recv_size += len(data)
                    f.write(data)
                else:
                    print "-->file %s transfer done!" % remote_filename
                    f.close()
            else:
                print "--> feedback info wrong:",feedback



    def list(self,msg): ## 查看文件列表
        print "<--> file",msg

    def interative(self): ## 交互界面
        while True:
            data_send = raw_input("My_FTP >> ").strip()
            if len(data_send) == 0:continue
            cmd = data_send.split()
            if hasattr(self,cmd[0]):
                func = getattr(self,cmd[0])
                func(cmd[1:])
            else:
                print "Wrong cmd usage!!"

            #self.tcpClient.sendall(data_send)
            #data_recv = self.tcpClient.recv(BUFSIZE)
            #if not data_recv:continue
            #print data_recv.strip()


    def connect(self): ## 连接建立和关闭
        self.tcpClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcpClient.connect((self.host,self.port))
        self.interative()


if __name__ == "__main__":
    HOST = "192.168.31.126"
    PORT = 9999

    ftp = MyFTP(HOST,PORT)
    ftp.connect()









