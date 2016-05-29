# slot_p1.py
# coding: utf-8
from types import MethodType
'''
1. 正常情况下，当我们定义了一个class，创建了一个class的实例后，
我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：


2. 还可以尝试给实例绑定一个方法：但是，
给一个实例绑定的方法，对另一个实例是不起作用的：

3. 为了给所有实例都绑定方法，可以给class绑定方法：

4. 但是，如果我们想要限制class的属性怎么办？
比如，只允许对Student实例添加name和age属性。
'''
class Student():
	__slots__ = ('name','age') #4. not working????
	


def set_age(self,age):
	self.age = age
def set_score(self,score):
	self.score = score
s = Student()
s.name = 'tom'  # 1. 
s.score = 101 #4
print s.name
s.set_age = MethodType(set_age, s, Student)  # 2. bind function to class
s.set_age(5)
print s.age

Student.set_score = MethodType(set_score,None, Student)
s.set_score(75)
print s.score
s3 = Student()
s3.set_score(88)


print s3.score