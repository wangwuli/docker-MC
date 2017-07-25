#!/usr/bin/python
#coding=UTF-8
from SocketServer import StreamRequestHandler,TCPServer,ThreadingTCPServer
import docker

HOST='127.0.0.1'
PORT=21567
ADDR=(HOST,PORT)
class MyRequestHandler(StreamRequestHandler):

	def handle(self):
		client = docker.from_env()
		print '..connected form :', self.client_address
 
		dictAll=eval(self.rfile.readline())
  
		if dictAll['connect_c']:     #docker操作命令
			if dictAll['command'] == 'list':
				print client.images.list()
				returnvalue = client.images.list()
			
			elif dictAll['command'] == 'add':     #请求添加
				pass
			elif dictAll['command'] == 'pull':      #下载镜像
				if dictAll['command'] == 'pullurl':   #从哪个镜像链接
					pass
			elif dictAll['command'] == 'run':    #启动
				pass
			elif dictAll['command'] == 'dokcetfile':  #创建
				pass
				
		elif dictAll['query']:    #收集系统信息
			pass
		elif dictAll['listen']:    #客户点监控命令
			pass
		
		
		self.wfile.write('%s' %returnvalue)
  
tcpServ = ThreadingTCPServer(ADDR,MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()
