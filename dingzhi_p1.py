# dingzhi_p1.py
# coding: utf-8
'''
1. 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类
2. such as __str__:
打印出一堆<__main__.Student object at 0x109afb190>，不好看。

怎么才能打印得好看呢？只需要定义好__str__()方法，
返回一个好看的字符串就可以了：
'''
class Student(object):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return 'Student object (name: %s)' % self.name   # 2
	__repr__ = __str__
Student('Tom')		

