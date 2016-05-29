# sorted_p1.py
mylist = [1,3,23,21,17,4]
print sorted(mylist)
def get_reverse(x,y):
	if x > y :
		return -1
	if x == y:
		return 0
	else:
		return 1
print sorted(mylist,get_reverse)