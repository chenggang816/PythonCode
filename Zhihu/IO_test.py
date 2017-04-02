# -*- coding: utf-8 -*-
import os
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
a = os.getcwd()
print a



b = '学习hello.txt'

print b
c = os.path.join(a,b)
print c

e = u'大卫·贝克汉姆'
print e
e1 = e.encode('gbk')
print e1

f = u'迪玛利亚（Ángel Di María）'
print f
f1 = f.encode('utf-8')
print f1
