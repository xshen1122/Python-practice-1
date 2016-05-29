# oop_p3.py
# coding: utf-8
'''
继承有什么好处？最大的好处是子类获得了父类的全部功能。
由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，
什么事也没干，就自动拥有了run()方法：
===
当子类和父类都存在相同的run()方法时，我们说，
子类的run()覆盖了父类的run()，在代码运行的时候，
总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态
===
看上去没啥意思，但是仔细想想，
现在，如果我们再定义一个Tort类型，也从Animal派生：
你会发现，新增一个Animal的子类，不必对run_twice()做任何修改，
实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，
原因就在于多态。

===
多态的好处就是，当我们需要传入Dog、Cat、Tort……时，
我们只需要接收Animal类型就可以了，
因为Dog、Cat、Tortoise……都是Animal类型，
然后，按照Animal类型进行操作即可。
由于Animal类型有run()方法，因此，传入的任意类型，
只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：
===
而当我们新增一种Animal的子类时，只要确保run()方法编写正确，
不用管原来的代码是如何调用的。这就是著名的“开闭”原则：

对扩展开放：允许新增Animal子类；

对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
'''
class Animal():
	def running(self):
		print 'Animal is running'
class Cat(Animal):
	def running(self):
		print 'Cat is running'
class Dog(Animal):
	def running(self):
		print 'Dog is running'
class Tort(Animal):
	def running(self):
		print 'Tort is running slowly'
def run_twice(tort):
	tort.running()
	tort.running()

animal = Animal()
dog = Dog()

cat = Cat()

run_twice(animal)
run_twice(cat)
run_twice(dog)
run_twice(Tort())