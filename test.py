#!/usr/bin/python
#coding=UTF-8
from socket import *


HOST = '127.0.0.1'
PORT = 21566
BUFSIZ = 1024
ADDR = (HOST,PORT)

data = {'connect_c':1,'query':0,'listen':0,'command':'list','ip':'127.0.0.1'}

data = str(data)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
	
tcpCliSock.send(('%s\r\n' %data).encode())
returnvalue = tcpCliSock.recv(BUFSIZ)

print returnvalue

tcpCliSock.close()