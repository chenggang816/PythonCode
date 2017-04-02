#!/usr /bin/env python
# -*- coding: utf-8 -*-

"""
抓取知乎话题中足球相关的问题，以xml格式文件保存抓取结果，
结果文件存放在data文件夹下
"""

import urllib
import urllib2
import re
import json
from Topic import *
from Content import *
import cookielib
import os
import sys
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import time
import random

def getTopics():
    zhihuTopics = []
    url = 'https://www.zhihu.com/topics'
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    request = urllib2.Request(url)
    response = opener.open(request)
    pattern = re.compile('<li.*?data-id="(.*?)"><a.*?>(.*?)</a></li>',re.S)
    results = re.findall(pattern,response.read().decode('utf-8'))
    for n1 in results:
        print n1[0],n1[1]
        topic = Topic(n1[0],n1[1])
        zhihuTopics.append(topic)
    return zhihuTopics

def getSubTopic(topic):
    url = 'https://www.zhihu.com/node/TopicsPlazzaListV2'
    isGet = True;
    offset = -20;
    contents = []
    while isGet:
        offset = offset + 20
        values = {'method': 'next', 'params': '{"topic_id":'+topic.id+',"offset":'+str(offset)+',"hash_id":""}'}
        try:
            data = urllib.urlencode(values)
            request = urllib2.Request(url,data,headers)
            response = urllib2.urlopen(request)
            json_str = json.loads(response.read().decode('utf-8'))
            # 将获取到的数组转换成字符串
            topicMsg = '.'.join(json_str['msg'])
            pattern = re.compile('href="/topic/(\d*?)">.*?<strong>(.*?)</strong>.*?<p>(.*?)</p>',re.S)
            results = re.findall(pattern,topicMsg)
            if len(results) ==0:
                isGet =False
            for n in results:
                content = Content(n[1],n[2])
                content.id = n[0]
                if hasExtracted(content):
                    continue
                contents.append(content)
                print '\n\n正在提取的子话题：',n[0],'->'+n[1],'\t详细:',n[2]
                t_start = time.time()
                getQuestions(n[0],n[1])
                t_stop = time.time()
                recordSubTopic(content)
                print '子话题%s提取完毕,用时 %s s' % (n[1],str(t_stop - t_start))
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"错误原因",e
    file = open(topic.name+'.txt','w')
    wiriteLog(contents,file)
    return contents
def hasExtracted(content):
    ctlxml = ET.ElementTree(file=getCtlXmlPath())
    root = ctlxml.getroot()
    for subTopic in root:
        if (subTopic.attrib['name'] == content.name) & (subTopic.attrib['id'] == content.id):
            return True
    return False
def getQuestions(subtopic_id,subtopic_name):
    page = 1
    url_prefix = 'https://www.zhihu.com/topic/%s/top-answers?page=' % subtopic_id
    index = 1
    xml_name = subtopic_name + subtopic_id + '.xml'
    xml_path = os.path.join(getDataDir(),xml_name.encode('gbk','ignore'))
    if os.path.exists(xml_path):
        os.remove(xml_path)
    root = ET.Element('SubTopic')
    root.set('id',subtopic_id)
    root.set('name',subtopic_name)
    request_timeout = 3
    error_times = 0
    while page <= 50:
        url = url_prefix + str(page)
        try:
            request_start = time.time()
            request = urllib2.Request(url,headers=headers)
            response = urllib2.urlopen(request,timeout=request_timeout)
            # time.sleep(random.random() * 5)
            pattern = re.compile(r'<a class="question_link".*?>\n*(.*?)\n*</a>.*?<span class="js-voteCount">(.*?)</span>.*?class="answer-date-link meta-item".*?>.*? (.*?)</a>',re.S)
            #.*?<textarea hidden.*?class="content">(.*?)</textarea>
            html = response.read()
            results = re.findall(pattern,html)
            request_stop = time.time()
            request_time = request_stop - request_start
            request_timeout = max(request_timeout * 0.6 + request_time * 0.4 + 3 , 3)
            # print u'\r本次请求用时:',request_time,' s',
            # sys.stdout.flush()
            # print u'\r下次请求超时时间：',request_timeout,' s',
            # sys.stdout.flush()
            for item in results:
                print '\r#',str(index),u'\t问题：',item[0],u"\t关注度:",item[1],
                sys.stdout.flush()
                question = ET.Element('q')
                question.set('t',item[2])
                question.set('i',str(index))
                votenum = ET.Element('v')
                votenum.text = item[1]
                title = ET.Element('t')
                title.text = item[0]
                # content = ET.Element('c')
                # content.text = item[2]
                question.append(votenum)
                question.append(title)
                # question.append(content)
                root.append(question)
                index = index + 1
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"错误原因：",e
                print u'当前页：',str(page)
                error_times = error_times + 1
                if error_times >= 3:
                    break
        finally:
            page = page + 1

    tree = ET.ElementTree(root)
    tree.write(xml_path,'UTF-8')
def recordSubTopic(content):
    xmlPath = getCtlXmlPath()
    ctlxml = ET.ElementTree(file=xmlPath)
    root = ctlxml.getroot()
    child = ET.Element('SubTopic')
    child.set('id',content.id)
    child.set('name',content.name)
    child.text = content.content
    root.append(child)
    ctlxml.write(xmlPath,'UTF-8')
    #ctlxml.write(sys.stdout)
def wiriteLog(contentes,file):
    for content in contentes:
        file.writelines(('\n'+content.name+'->'+content.content).encode("UTF-8"))

def getDataDir():
    cwd = os.getcwd()
    dataDir = os.path.join(cwd,'data')
    if not os.path.exists(dataDir):
        os.makedirs(dataDir)
    return dataDir
def getCtlXmlPath():
    data = getDataDir()
    return os.path.join(data,'ctl.xml')
def writeCtlXmlRoot(topic):
    xmlPath = getCtlXmlPath()
    if os.path.exists(xmlPath):
        return
    root = ET.Element('Topic')
    t_name = topic.name.encode('utf-8')
    root.set('name',t_name)
    root.set('id',topic.id)
    tree = ET.ElementTree(root)
    tree.write(xmlPath,'UTF-8')
    #tree.write(sys.stdout)

reload(sys)
sys.setdefaultencoding('utf-8')

print '开始拉取数据...\n'
headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0',
           'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
           'X-Requested-With':'XMLHttpRequest',
           'Referer':'https://www.zhihu.com/topics',
           'Cookie':'__utma=51854390.517069884.1416212035.1416212035.1416212035.1; q_c1=c02bf44d00d240798bfabcfc95baeb56|1455778173000|1416205243000; _za=b1c8ae35-f986-46a2-b24a-cb9359dc6b2a; aliyungf_tc=AQAAAJ1m71jL1woArKqF22VFnL/wRy6C; _xsrf=9d494558f9271340ab24598d85b2a3c8; cap_id="MDNiMjcwM2U0MTRhNDVmYjgxZWVhOWI0NTA2OGU5OTg=|1455864276|2a4ce8247ebd3c0df5393bb5661713ad9eec01dd"; n_c=1; _alicdn_sec=56c6ba4d556557d27a0f8c876f563d12a285f33a'
           }

i = 0
topics = getTopics()
for topic in topics:
    if topic.name == u'足球':
        print '大主题：',topic.name
        writeCtlXmlRoot(topic)
        content = getSubTopic(topic)
        i +=len(content)
print '知乎总话题数为：'+str(i) #知乎总话题数为：15769  关于足球的知乎总话题数为：122
print '拉取数据结束'