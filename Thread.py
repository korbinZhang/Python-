#coding=utf-8
#python线程学习实例
import threading
from time import ctime,sleep
import os
def one(i):
	print "i"+str(i)+"start..."
	sleep(i)
	if i%10 == 0:
		sleep(5)
	print "i"+str(i)+"end"
threads = []
for url in range(1,100):
	t = threading.Thread(target=one,args=(url,))
	threads.append(t)

if __name__ == '__main__':
	for t in threads:
		t.setDaemon(True)
		t.start()
	os.system('pause')