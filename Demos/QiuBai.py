import urllib
import urllib2
import re


page = 1
url = 'http://www.qiushibaike.com/8hr/page/' + str(page) + '/?s=4938943'
user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
headers = {'User-Agent':user_agent}
try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    content = response.read()
    #print content
    pattern = re.compile(r'<div.*?class="content">.*?<span>(.*?)</span>.*?</div>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print item
        print '\n'
except urllib2.URLError,e:
    if hasattr(e,'code'):
        print e.code
    if hasattr(e,'reason'):
        print e.reason