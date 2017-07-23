from django.http import HttpResponse
import docker

def main(request):
    return HttpResponse("Hello world")

def list(request):     #查看
	hwho = request.GET.get('who')
	client = docker.from_env()
	if hwho == "all":
		return HttpResponse(client.containers.list(all=True))	
	elif hwho == "run":
		return HttpResponse(client.containers.list())
	else:
		return HttpResponse("what are you doing !")

def pull(request):
	name = request.GET.get('name')
	client = docker.from_env()
	return HttpResponse(client.images.pull('centos'))

	#name = request.GET.get('name')
	#if repository:
	#
	
	#client.images.pull(tag='busybox',repository='192.168.0.1:8000')
	#TypeError: pull() takes at least 2 arguments (2 given)
	
	#client.images.pull(repository='192.168.0.1:8000/busybox')
	#TypeError: pull() takes at least 2 arguments (1 given)
	
	#client.images.pull('centos',repository='192.168.0.1:8000')
	#TypeError: pull() got multiple values for keyword argument 'repository'
	
	#repository。。。。???
	"""
		pull(self, name, tag=None, **kwargs)。。。
	    Args:
        repository (str): The repository to pull
        tag (str): The tag to pull
        insecure_registry (bool): Use an insecure registry
        auth_config (dict): Override the credentials that
            :py:meth:`~docker.client.DockerClient.login` has set for
            this request. ``auth_config`` should
	"""