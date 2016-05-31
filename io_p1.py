# io_p1.py
# coding: utf-8
'''
很明显，使用异步IO来编写程序性能会远远高于同步IO，
但是异步IO的缺点是编程模型复杂。想想看，你得知道什么时候通知你“汉堡做好了”，
而通知你的方法也各不相同。如果是服务员跑过来找到你，这是回调模式，
如果服务员发短信通知你，你就得不停地检查手机，这是轮询模式。
总之，异步IO的复杂度远远高于同步IO。
callback()
1. 操作IO的能力都是由操作系统提供的，
每一种编程语言都会把操作系统提供的低级C接口封装起来方便使用，
Python也不例外。我们后面会详细讨论Python的IO编程接口。
2. 使用with语句操作文件IO是个好习惯
'''
with open('slot_p1.py', 'r') as f:
	f.read()
try:
	myfile = open('slot-p1.py','r')
except IOError:
	print 'the file doesn\'t exist'
	raise IOError

print myfile.read()
myfile.close()