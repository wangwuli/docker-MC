#coding=utf-8
from django.http import HttpResponse
import docker


def main(request):
    return HttpResponse("Hello world")

def list(request):       #查看	
	ip = request.GET.get('ip')
	hwho = request.GET.get('who')
	
	client = docker.from_env()
	if hwho == "all":
		return HttpResponse(client.containers.list(all=True))	
	elif hwho == "run":
		return HttpResponse(client.containers.list())
	else:
		return HttpResponse("what are you doing !")

def pull(request):         #镜像下载
	getdisk=request.GET.get
	name = request.GET.get('name')
	client = docker.from_env()
	
	name = request.GET.get('name')
	if repository:
		client.images.pull('127.0.0.1:5000/nginx')
	else:
		return HttpResponse(client.images.pull('centos'))