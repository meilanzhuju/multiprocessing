import random
import time
import threading

#方法一：把一个函数传入Thread实例，然后调用start方法开始执行
#新进程执行的代码
def thread_run(urls):
	print("Current %s is running ..." % threading.current_thread().name)
	for url in urls:
		print("%s ------>>> %s" % (threading.current_thread().name, url))
		time.sleep(random.random())
	print("%s ended." % threading.current_thread().name)
	
print("%s is running ..." % threading.current_thread().name)
t1 = threading.Thread(target=thread_run, name="Thread_1", args=(['url_1', 
							'url_2', 'url_3'],))
t2 = threading.Thread(target=thread_run, name="Thread_2", args=(['url_4',
							'url_5', 'url_6'],))
t1.start()
t2.start()
t1.join()
t2.join()
print("%s ended." % threading.current_thread().name)
