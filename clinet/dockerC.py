#!/usr/bin/python
#coding=UTF-8
from SocketServer import StreamRequestHandler,TCPServer,ThreadingTCPServer
from time import ctime

HOST=''
PORT=21567
ADDR=(HOST,PORT)
class MyRequestHandler(StreamRequestHandler):

	def handle(self):
		print '..connected form :', self.client_address
 
		dictAll=eval(self.rfile.readline())
  #serverM send "{'A':'aa'}"
  
		if dictAll['list']:     #查询
			pass
		elif dictAll['add']:     #请求添加
			pass
		elif dictAll['pull']:      #下载镜像
			dictAll['pullurl']    #从哪个镜像链接
		elif dictAll['run']:    #启动
			pass
		elif dictAll['dokcetfile']:  #创建
			pass
  
tcpServ = ThreadingTCPServer(ADDR,MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()
