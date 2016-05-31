# error_p1.py
# coding: utf-8
import logging
'''
所以高级语言通常都内置了一套
try...except...finally...的错误处理机制，Python也不例外。
1. 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，
即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，
至此，执行完毕。
2. baseError, refer to https://docs.python.org/2/library/exceptions.html#exception-hierarchy
3. 也就是说，不需要在每个可能出错的地方去捕获错误，
只要在合适的层次去捕获错误就可以了。
这样一来，就大大减少了写try...except...finally的麻烦。
4. Python内置的try...except...finally用来处理错误十分方便。出错时，
会分析错误信息并定位错误发生的代码位置才是最关键的。

程序也可以主动抛出错误，让调用者来处理相应的错误。
但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因
logging.exception(e)
5. 抛出错误
在bar()函数中，我们明明已经捕获了错误，但是，打印一个Error!后，
又把错误通过raise语句抛出去了，这不有病么？

其实这种错误处理方式不但没病，而且相当常见。
捕获错误目的只是记录一下，便于后续追踪。
但是，由于当前函数不知道应该怎么处理该错误
所以，最恰当的方式是继续往上抛，让顶层调用者去处理。
'''
def chufa(x,y):
	try:
		return x/y
	except ZeroDivisionError:
		print 'donnot allow 0'

	finally:
		print x/y	
		print 'fianlly....'
# chufa(4,2)

# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     try:
#         bar('0')
#     except StandardError, e:
#         logging.exception(e)   #4
#     finally:
#         print 'finally...'
# if __name__ == '__main__':
# 	main()

def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        raise      #5

def main():
    bar('0')

main()