#!/usr/bin/env python
import datetime
from dateutil import parser
import urllib2
from bs4 import BeautifulSoup

article_url = 'http://www.usmagazine.com/entertainment/news/kim-kardashian-worries-over-247-security-after-paris-robbery-w464533'

soup = BeautifulSoup(urllib2.urlopen(article_url).read(),'html.parser')

title = soup.h1.contents[0]
print title

article_date = soup.time.contents[0]
try:
    article_date = parser.parse(article_date, fuzzy=True)
except:
    print('ERROR ON', article_date)
    raise
print article_date

article_text = soup.main
[aside.extract() for aside in article_text.find_all("aside")]
print article_text.get_text()
