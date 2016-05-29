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



'''