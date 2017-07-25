#!/usr/bin/python
#coding=UTF-8
from socket import *
from SocketServer import StreamRequestHandler,TCPServer,ThreadingTCPServer

def linkclient(data,ip):
	HOST = ip
	PORT = 21567
	BUFSIZ = 1024
	ADDR = (HOST,PORT)

	tcpCliSock = socket(AF_INET,SOCK_STREAM)
	tcpCliSock.connect(ADDR)
	
	tcpCliSock.send(('%s\r\n' %data).encode())
	returnvalue = tcpCliSock.recv(BUFSIZ)
	
	tcpCliSock.close()
	return returnvalue


HOST='127.0.0.1'
PORT=21566
ADDR=(HOST,PORT)

class MyRequestHandler(StreamRequestHandler):

	def handle(self):
		# print '..connected form :', self.client_address
 
		dictAll=eval(self.rfile.readline())
		#serverM send "{'A':'aa'}"
		if dictAll['connect_c']:          #docker操作命令,直接转发客户端
			
			if dictAll['command'] == 'list':         #查询				
				returnvalue = linkclient(dictAll,dictAll['ip'])
				print(returnvalue)

		elif dictAll['query']:     #手机信息，写入数据库
			pass
		elif dictAll['listen']:    #监控相关，写入数据库，触发告警
			pass
		
		
		self.wfile.write('%s' %returnvalue)
		
tcpServ = ThreadingTCPServer(ADDR,MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()

	
	

