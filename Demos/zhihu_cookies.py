#-*- coding:utf-8 -*-
import urllib
import urllib2
import re
import time
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import cookielib

def post(url, data,cookiestr):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    headers = {'User-Agent':user_agent,'cookie':cookiestr,
               # 'Origin': 'https://www.zhihu.com',
               'Referer': 'https://www.zhihu.com/',
               # 'Host': 'www.zhihu.com',
               # 'Connection': 'keep-alive',
               # 'Content-Length': '68',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               #  'Accept': '*/*',
                'X-Requested-With': 'XMLHttpRequest',
                # 'X-Xsrftoken': 'b28618368ae60513d643194f7f3a9141',
                # 'Accept-Encoding': 'gzip, deflate, br',
                # 'Accept-Language': 'zh-CN,zh;q=0.8'
               }

    data = urllib.urlencode(data)
    req = urllib2.Request(url,data,headers=headers)
    #enable cookie
    # cookiefile = "cookiefile"
    # cookieJar = cookielib.MozillaCookieJar(cookiefile)
    # opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar));

    response = urllib2.urlopen(req)
    # response = urllib2.urlopen(req)
    text = response.read()
    print text
    print len(text)
    # cookieJar.save()
    #print response.read()

    #second http request use cookie
    # cookieJar = cookielib.MozillaCookieJar(cookiefile)
    # cookieJar.load()
    # #url = "http://www.xiami.com"
    # opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
    # response = opener.open(url)
    # print response.read()

name = '15629101900'
pwd = 'cg123456'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.zhihu.com/#signin")

wait = WebDriverWait(webdriver,15)

ele_name = driver.find_element_by_name('account')
ele_name.send_keys(name)
ele_pwd = driver.find_element_by_name('password')
ele_pwd.send_keys(pwd)

ele = wait.until(lambda webdriver:driver.find_element_by_id('zh-home-list-title'))

print driver.get_cookies()
dict_cookies = {}
for item in driver.get_cookies():
    if not item["name"] in dict_cookies:
        dict_cookies[item["name"]] = item["value"]
#get the session cookie
cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
print cookie

cookiestr = ';'.join(item for item in cookie)
print cookiestr
# homeurl = driver.current_url
homeurl = 'https://www.zhihu.com/node/TopStory2FeedList'
print 'homeurl: %s' % homeurl
headers = {'cookie':cookiestr}
req = urllib2.Request(homeurl, headers = headers)
data = {"method":"next","params":{"offset":10,"start":"15"}}

post(homeurl,data,cookiestr)

#response = urllib2.urlopen(req,data)
#result = requests.post(homeurl,{"offset":10,"start":"15"},cookies = dict_cookies)
#text = response.read()
#print text
# fd = open('homepage.html', 'w')
# fd.write(text)
# fd.close()
# print result.text

#time.sleep(20)

