# module_p1.py
# coding: utf-8
'''
举个例子，一个abc.py的文件就是一个名字叫abc的模块，
一个xyz.py的文件就是一个名字叫xyz的模块
引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。
现在，abc.py模块的名字就变成了mycompany.abc，
类似的，xyz.py的模块名变成了mycompany.xyz。

'''
' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print 'Hello, world!'
    elif len(args)==2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__=='__main__':
    test()
'''
导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，
就可以访问sys模块的所有功能。

sys模块有一个argv变量，用list存储了命令行的所有参数。
argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：

运行python hello.py获得的sys.argv就是['hello.py']；

运行python hello.py Michael获得的sys.argv就是['hello.py', 'Michael]。

=====

当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量
__name__置为__main__，而如果在其他地方导入该hello模块时，
if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，
最常见的就是运行测试。


'''
'''
What's __xxx__?
类似__xxx__这样的变量是特殊变量，可以被直接引用，
但是有特殊用途，比如上面的__author__，__name__就是特殊变量，
hello模块定义的文档注释也可以用特殊变量__doc__访问，
我们自己的变量一般不要用这种变量名；
'''

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
'''
我们在模块里公开greeting()函数，
而把内部逻辑用private函数隐藏起来了，
这样，调用greeting()函数不用关心内部的private函数细节，
这也是一种非常有用的代码封装和抽象的方法，即：

外部不需要引用的函数全部定义成private，
只有外部需要引用的函数才定义为public。

'''