# decorator_p1.py
# coding: utf-8
'''
由于函数也是一个对象，
而且函数对象可以被赋值给变量，
所以，通过变量也能调用该函数。

'''
def now():
	print '2016-5-29'
f = now
print f.__name__
print now.__name__
'''
现在，假设我们要增强now()函数的功能，
比如，在函数调用前后自动打印日志，
但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，
称之为“装饰器”（Decorator）。

'''
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
@log
def now():
    print '2013-12-25'
now()