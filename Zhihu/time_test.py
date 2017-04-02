import time

a = time.time()
c = time.clock()
print a,c
time.sleep(2.567567567)
b = time.time()
d = time.clock()
print b - a
print d - c