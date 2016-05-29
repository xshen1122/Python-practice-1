# unittest_p1.py
# coding: utf-8
'''
比如对函数abs()，我们可以编写出以下几个测试用例：

    输入正数，比如1、1.2、0.99，期待返回值与输入相同；

    输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；

    输入0，期待返回0；

    输入非数值类型，比如None、[]、{}，期待抛出TypeError。


'''
import unittest
from mydict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()