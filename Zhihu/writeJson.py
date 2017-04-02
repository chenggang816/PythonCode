#!/usr /bin/env python
# -*- coding: utf-8 -*-

"""
读取result.txt文件的内容，组织成json格式
使用json.dumps 将 json 格式的数据写到data.json文件里
"""

def store(data):
    import json
    with open('data.json', 'w') as f:
        d = json.dumps(data,ensure_ascii=False,indent=2)
        f.write(d)

if __name__ == "__main__":
    data = []
    i = 1
    for line in open('result.txt'):
        line = line.rstrip('\n')
        s = line.split('\t\t\t')
        item = {}
        item['num'] =  i
        item['word'] = s[0]
        item['count'] = s[1]
        i = i+1
        data.append(item)
    store(data)
