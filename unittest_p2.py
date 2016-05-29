# unittest_p2.py
# coding: utf-8
'''

比如对函数abs()，我们可以编写出以下几个测试用例：

    输入正数，比如1、1.2、0.99，期待返回值与输入相同；

    输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；

    输入0，期待返回0；

    输入非数值类型，比如None、[]、{}，期待抛出TypeError。




'''
from Myabs import Myabs
import unittest
class TestMy(unittest.TestCase):

    def test_zhengshu(self):
    	d = Myabs(12)
    	self.assertEquals(d.Myabs(), 12)
    def test_xiaoshu(self):
    	d = Myabs(0.99)
    	self.assertEquals(d.Myabs(), 0.99)
    def test_minus(self):
    	d = Myabs(-0.99)
    	self.assertEquals(d.Myabs(),0.99)
    def test_zero(self):
    	d = Myabs(0)
    	self.assertEquals(d.Myabs(),0)
    def test_typeerror(self):
    	d = Myabs('[]')
    	self.assertEquals(d.Myabs(), TypeError)
if __name__ == '__main__':
    unittest.main()