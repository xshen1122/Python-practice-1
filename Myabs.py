# Myabs.py
class Myabs():
	def __init__(self,a):
		self.a = a
	def Myabs(self):
		if type(self.a) in [int, float]:
			return abs(self.a)
		else:
			return TypeError
