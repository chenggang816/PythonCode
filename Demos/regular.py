# -*-coding:utf-8-*-

import re
pattern = re.compile('hello')

r1 = re.match(pattern,'1hello')
if r1:
    print r1.group()
else:
    print '1not match!'

r2 = re.match(pattern,'helloo CQC')
if r2:
    print r2.group()
else:
    print '2not match!'

r3 = re.match(pattern,'helo CQC')
if r3:
    print r3.group()
else:
    print '3not match!'

r4 = re.match(pattern,'hello CQC')
if r4:
    print r4.group()
else:
    print '4not match!'

pattern = re.compile('a(.*?)b',re.S)
s = 'aabacba dafba  sa'
print re.findall(pattern,s)

pattern = re.compile(r'<a class="question_link".*?>\n*(.*?)\n*</a>.*?<a.*?zm-item-vote-count js-expand js-vote-count.*?>(\d*?)</a>',re.S)
s = u'''
<div class="feed-content" data-za-module="AnswerItem">
<meta itemprop="answer-id" content="7102362" />
<meta itemprop="answer-url-token" content="29297718" />
<h2 class="feed-title"><a class="question_link" href="/question/24862074#answer-7102362" target="_blank" data-id="2126809" data-za-element-name="Title">
为什么中国古代的贵族氏族没有设立家徽的传统？
</a></h2>
<div class="feed-question-detail-item">

<a href="#" class="toggle-expand btn-toggle-question-detail ellipsis js-expandQuestionDetail">像西方的贵族和日本的贵族们大多都有自己的...?<span>显示问题详情</span></a>
<div class="question-description zm-editable-content">
像西方的贵族和日本的贵族们大多都有自己的家徽，为什么中国古代的贵族却没有？<br />日本战国贵族的 <a href="//link.zhihu.com/?target=http%3A//zh.wikipedia.org/wiki/%25E5%25AE%25B6%25E7%25B4%258B" class=" wrap external" target="_blank" rel="nofollow noreferrer">家紋<i class="icon-external"></i></a><br />西方国家 <a href="//link.zhihu.com/?target=http%3A//zh.wikipedia.org/wiki/%25E7%25B4%258B%25E7%25AB%25A0%25E5%25AD%25B8" class=" wrap external" target="_blank" rel="nofollow noreferrer">纹章学<i class="icon-external"></i></a>
</div>

</div>
<div class="expandable entry-body">
<link itemprop="url" href="/question/24862074/answer/29297718" />
<!-- <meta itemprop="answer-id" content="7102362">
<meta itemprop="answer-url-token" content="29297718"> -->

<div class="zm-item-vote">
<a class="zm-item-vote-count js-expand js-vote-count" href="javascript:;" data-bind-votecount="">4794</a>
</div>

<div class="zm-votebar" data-za-module="VoteBar">
<button class="up" aria-pressed="false" title="赞同">
<i class="icon vote-arrow"></i>
<span class="count">4794</span>
<span class="label sr-only">赞同</span>
</button>
<button class="down" aria-pressed="false" title="反对，不会显示你的姓名">
<i class="icon vote-arrow"></i>
<span class="label sr-only">反对，不会显示你的姓名</span>
</button>
</div>



<div class="zm-item-answer-author-info">

<span class="summary-wrapper">
<span class="author-link-line">'''
items = re.findall(pattern,s)
if items:
    for item in items:
        print u"关注度:",item[1],u'问题：',item[0]
else:
    print u'没有找到匹配项！'