# oop_p1.py
# coding: utf-8
'''
面向对象的设计思想是从自然界中来的，
因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。
Class是一种抽象概念，
比如我们定义的Class——Student，是指学生这个概念，
而实例（Instance）则是一个个具体的Student，
比如，Bart Simpson和Lisa Simpson是两个具体的Student：

所以，面向对象的设计思想是抽象出Class，根据Class创建Instance。

面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。
数据封装、继承和多态是面向对象的三大特点，我们后面会详细讲解。

'''
class Student():
	def __init__(self, name, score):
		self.name = name
		self.score = score # variables
	def print_name(self):
		print self.name  # method
	def print_score(self):
		print self.score
	def print_grade(self):
		if self.score > 90:
			print self.name + ' is A'
		elif self.score > 60:
			print self.name + ' is B'
		else:
			print self.name + ' is C'
class China_Student(Student):
	def __init__(self,name,score,country):
		Student.__init__(self,name,score)
		self.country = country
	
	def print_country(self):
		print self.country
bob = Student('bob',91)
tom = Student('tom', 61)
print bob.name
bob.print_grade()
zhangshan = China_Student('zhangshan',80,'China')
zhangshan.print_grade()
'''
这样一来，我们从外部看Student类，就只需要知道，
创建实例需要给出name和score，而如何打印，
都是在Student类的内部定义的，这些数据和逻辑被“封装”起来了，
调用很容易，但却不用知道内部实现的细节。

封装的另一个好处是可以给Student类增加新的方法，比如get_grade：

====
类是创建实例的模板，而实例则是一个一个具体的对象，
各个实例拥有的数据都互相独立，互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，
但无需知道方法内部的实现细节。

和静态语言不同，Python允许对实例变量绑定任何数据，
也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，
但拥有的变量名称都可能不同：
'''