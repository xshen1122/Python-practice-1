# reduce_p1.py
# coding: utf-8
'''
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，
可以接受一个list并利用reduce()求积。
'''
my_list = [ 1,2,3,4,5,6]
def prod(x,y):
	return x*y
print reduce(prod,my_list)
