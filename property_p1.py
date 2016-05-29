# property_p1.py
# coding: utf-8
'''
1. Python内置的@property装饰器就是负责把一个方法变成属性调用的：
2. @property的实现比较复杂，我们先考察如何使用。
把一个getter方法变成属性，只需要加上@property就可以了，
此时，@property本身又创建了另一个装饰器@score.setter，
负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
3. @property广泛应用在类的定义中，可以让调用者写出简短的代码，
同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
'''
class Student(object):
    @property
    def score(self):  # 2
        return self._score
    @score.setter   #2
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

tom = Student()
tom.score = 60
print tom.score
tom.score = 999
print tom.score

class Person(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth