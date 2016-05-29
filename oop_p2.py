# oop_p2.py
# coding: utf-8
'''
改完后，对于外部代码来说，没什么变动，
但是已经无法从外部访问实例变量.__name和实例变量.__score了

这样就确保了外部代码不能随意修改对象内部的状态，
这样通过访问限制的保护，代码更加健壮。

但是如果外部代码要获取name和score怎么办？
可以给Student类增加print_name和print_score这样的方法：

===
如果又要允许外部代码修改score怎么办？可以给Student类增加set_score方法：

===
需要注意的是，在Python中，变量名类似__xxx__的，
也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
特殊变量是可以直接访问的，不是private变量，
所以，不能用__name__、__score__这样的变量名。

'''
class Student():
	def __init__(self, name, score):
		self.__name = name
		self.__score = score # variables
	def set_name(self,name):
		self.__name = name
	def return_name(self):
		return self.__name
	def print_name(self):
		print self.__name  # method
	def print_score(self):
		print self.__score
	def print_grade(self):
		if self.__score > 90:
			print self.__name + ' is A'
		elif self.__score > 60:
			print self.__name + ' is B'
		else:
			print self.__name + ' is C'
class China_Student(Student):
	def __init__(self,name,score,country):
		Student.__init__(self,name,score)
		self.__country = country
	
	def print_country(self):
		print self.__country
bob = Student('bob',91)
tom = Student('tom', 61)
print bob.return_name()
bob.set_name('kelly')
print bob.return_name()
bob.print_grade()
zhangshan = China_Student('zhangshan',80,'China')
zhangshan.print_grade()