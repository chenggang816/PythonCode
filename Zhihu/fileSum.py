#!/usr /bin/env python
# -*- coding: utf-8 -*-

"""
读取data文件夹下所有xml文件的内容，解析xml，
提取出知乎问题，按行写入allqs.txt文件中
"""

import os
try:
    import xml.etree.cElementTree as ET
except:
    import xml.etree.ElementTree as ET

def getDataDir():
    cwd = os.getcwd()
    dataDir = os.path.join(cwd,'data')
    if not os.path.exists(dataDir):
        os.makedirs(dataDir)
    return dataDir

def extractQuestions(agr,dirname,names):
    global i,f
    names = [os.path.join(dirname,n) for n in names if os.path.isfile(os.path.join(dirname,n)) and n != 'ctl.xml']
    for n in names:
        tree = ET.ElementTree(file = n)
        root = tree.getroot()
        for q in root:
            i= i + 1
            t = q.find('t')
            f.write(t.text.encode('utf-8') + '\n')

global i,f
file_allqs = os.path.join(os.getcwd(),'allqs.txt')
with open(file_allqs,'w') as f:
    i = 0
    os.path.walk(getDataDir(),extractQuestions,'')
    print i