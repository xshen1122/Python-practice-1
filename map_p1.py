# coding: utf-8
# map_p1.py
'''
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
其他小写的规范名字。输入：['adam', 'LISA', 'barT']，
输出：['Adam', 'Lisa', 'Bart']
'''
def return_correct(str1):
	new_str1 = str1[0].upper()
	for item in str1[1:]:
		new_str1 += item.lower()
	return new_str1
str_list = ['adam', 'LISA', 'barT']
print map(return_correct, str_list)