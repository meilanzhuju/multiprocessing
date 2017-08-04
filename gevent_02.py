from gevent import monkey; monkey.patch_socket()
import gevent

def f(n):
	for i in range(n):
		print()