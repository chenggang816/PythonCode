# -*- coding: utf-8 -*-
# tankywoo@2013-05-24

import sys
from time import sleep
print 'a'
for i in range(1,5):
    print "\rHello, Gay! ",i,u'个',
    sys.stdout.flush()
    sleep(1)