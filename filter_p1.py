# filter_p1.py
#  coding: utf-8
'''
请尝试用filter()删除1~100的素数
'''
def is_zhishu(x):
	flag = True
	for item in range(2,x):
		if x % item == 0:
			flag = flag * False
		else:
			flag = flag * True
	return flag
my_list=[]
for item in range(1, 100+1):
	my_list.append(item)
print filter(is_zhishu, my_list)