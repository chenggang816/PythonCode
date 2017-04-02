#-*- coding:utf-8 -*-
import urllib
import urllib2
import re
import time
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
start = time.time()
while True:
    js = "window.scrollTo(0,document.body.scrollHeight)"
    driver.execute_script(js)
    try:
        #wait = WebDriverWait(webdriver,20)
        wait.until(lambda webdriver:driver.find_element_by_id('zh-load-more'))
    except:
        break
    stop = time.time()
    if stop - start > 15:
        break

#parse page source
pattern = re.compile(r'<a class="question_link".*?>\n*(.*?)\n*</a>.*?<a.*?zm-item-vote-count js-expand js-vote-count.*?>(.*?)</a>',re.S)
print driver.page_source
items = re.findall(pattern,driver.page_source)
if items:
    index = 1
    for item in items:
        print '#',str(index),u"\t关注度:",item[1],u'\t问题：',item[0]
        index = index + 1
else:
    print u'没有找到匹配项！'