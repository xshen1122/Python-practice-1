# jicheng_p1.py
# coding: utf-8
'''
正确的做法是采用多重继承。首先，主要的类层次仍按照哺乳类和鸟类设计：

现在，我们要给动物再加上Runnable和Flyable的功能，
只需要先定义好Runnable和Flyable的类：

3. 通过多重继承，一个子类就可以同时获得多个父类的所有功能。
===
1. Mixin

在设计类的继承关系时，通常，主线都是单一继承下来的，
例如，Ostrich继承自Bird。
但是，如果需要“混入”额外的功能，通过多重继承就可以实现，
比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为Mixin。

2. Mixin的目的就是给一个类增加多个功能，
这样，在设计类的时候，我们优先考虑通过多重继承来组合多个Mixin的功能，
而不是设计多层次的复杂的继承关系。
'''
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal, Runnable):
    pass

class Bat(Mammal,Flyable):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass


bat = Bat()
bat.fly()
dog = Dog()
dog.run()