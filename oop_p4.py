# oop_p4.py
# coding: utf-8
'''
change __len__

'''

class myclass(object):
	def __len__(self):
		return 10

myclass1 = myclass()
print myclass1.__len__()
print len(myclass1)

class myobject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x
myobject1 = myobject()
print hasattr(myobject1,'x')

setattr(myobject1,'y',2)
print getattr(myobject,'y')