#-*- coding:utf-8 -*-
import urllib
import urllib2
import re

class news_scrap(object):
    def __init__(self):
        self.url = 'http://news.163.com/'
        self.user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
        self.headers = {'User-Agent':self.user_agent}
        self.urls = set([])
        self.urlIndex = 1
        self.__addUrl__()
    def __addUrl__(self):
        self.urls.add(self.url)
    def __existsUrl__(self,url):
        return url in self.urls
    def __isNewsUrl__(self):
        pattern = re.compile(r'http://news.163.com/16/\d{4}/\d{2}/.*?\.html')
        return re.match(pattern,self.url)
    def __storeNews__(self,url):
        pass
    def getNews(self):
        try:
            request = urllib2.Request(self.url,headers=self.headers)
            print u'加载中...'
            response = urllib2.urlopen(request)
            content = response.read()
            #print content
            pattern = re.compile(r'<a.*?href="(.*?)".*?</a>',re.S)
            items = re.findall(pattern,content)
            childUrls = set([])
            for item in items:
                isWYAddress = item.startswith("http://news.163.com/16")
                isNew = not self.__existsUrl__(item)
                if isWYAddress&isNew:
                    print '#\t',str(self.urlIndex),':',item
                    self.urlIndex = self.urlIndex + 1
                    self.__addUrl__()
                    childUrls.add(item)
            for u in childUrls:
                self.url = u
                if self.__isNewsUrl__():
                    self.__storeNews__(item)
                self.getNews()
        except urllib2.URLError,e:
            if hasattr(e,'code'):
                print e.code
            if hasattr(e,'reason'):
                print e.reason
if __name__ == '__main__':
    ns = news_scrap()
    ns.getNews()