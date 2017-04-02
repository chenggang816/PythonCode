#!/usr/bin/env python
#-*-coding:utf-8-*-
#python

print 'hello,world';
print '100+100=',100+100
print u'中文'
#name = raw_input("姓名：".decode('utf-8').encode('gbk'))
#print u'%s'.encode('gbk') % name

#list
classmates=['Jane','Michael','Bob']
classmates[0]
classmates[-1]
classmates.append('Lucy')
classmates.pop()
classmates.pop(-1)
L = [123,'abc',True]

#tuple
classmates = ('Michael', 'Bob', 'Tracy')
t = (1,)

#if
age = -20
if age>18:
	print "your age is:",age,",adult"
elif age<0:
	print "input error!"
else:
	print "your age is:",age,",child"
	
#for
names = ['a','b','c']
for x in names:
	print x
sum = 0
for x in range(101):
	sum += x
print sum

#while
n = 0
while n<100:
	n = n + 1;
print n

#int()
#n = raw_input("birth year:")
n='1994'
n = int(n)
if n>2000:
	print u'00后'
else:
	print u'00前'
	
#dict
d = {'cg':23,'lf':24,'ywb':22,'wt':23}
d.update({'zzb':23})
for item in d:
	print item,':',d[item]
		
#set
s1 = set([1,2,4,4,5,5,6])
s2 = set([4,5,6,6,6,4,7])
print s1
print s2
print s1 & s2
print s1 | s2

#function
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad oparand type')
	if x > 0:
		return x
	else:
		return -x

print my_abs(-100)
#my_abs('A')
def calc(*num):
	s = 0
	for i in num:
		s = s+i*i
	return s
print calc(1,2,3)
print calc(*s1)

#slice
print '\nslice test'
L = range(30)
print L
print L[2:5]
print L[:10]
print L[-10:]
print L[::10]

for i,n in enumerate([10,30,20]):
	print i,n
print '\n'


#list generator
L1 = [m+n for m in 'ABC' for n in '123']
print L1
L1 = [i.lower() for i in L1]
print L1

#isinstance
x = 123
print isinstance(x,str)

#generator
g = (x * x for x in range(10))
print g.next()
for i in g:
	print i
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b=b,a+b
		n = n+1		
print 'fib:'
for n in fib(10):
	print n
	