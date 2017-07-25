#coding=utf-8
from django.http import HttpResponse
import docker
from socket import *

def link(command,dockerip,connect_c=0,query=0,listen=0):
	HOST = '127.0.0.1'
	PORT = 21566
	BUFSIZ = 1024
	ADDR = (HOST,PORT)
	
	data = {'connect_c':connect_c,'query':query,'listen':listen,'command':command,'ip':dockerip}
	
	data = str(data)
	
	tcpCliSock = socket(AF_INET,SOCK_STREAM)
	tcpCliSock.connect(ADDR)
	
	tcpCliSock.send(('%s\r\n' %data).encode())
	returnvalue = tcpCliSock.recv(BUFSIZ)
	
	tcpCliSock.close()
	return returnvalue


def main(request):
    return HttpResponse("Hello world")

def list(request):       #查看	
	dockerip = request.GET.get('dockerip')
	command = request.GET.get('command')
	
	client = docker.from_env()
	if command == "list":
		returnvalue= link(command,dockerip,connect_c=1)
		return HttpResponse(returnvalue)
	else:
		return HttpResponse("what are you doing !")

# def pull(request):         #镜像下载
	# getdisk=request.GET.get
	# name = request.GET.get('name')
	# client = docker.from_env()
	
	# name = request.GET.get('name')
	# if repository:
		# client.images.pull('127.0.0.1:5000/nginx')
	# else:
		# return HttpResponse(client.images.pull('centos'))