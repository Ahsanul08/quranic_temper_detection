# -*- coding: UTF-8 -*-

import re
import requests
import urllib2
from bs4 import BeautifulSoup


def parse(url):
    soup = BeautifulSoup(urllib2.urlopen(url).read().decode('utf-8'),'lxml')
    phrases_to_check = [i.text for i in soup.find_all('p',text = re.compile(ur'[\u0600-\u06FF]+'))]
    #print "\n\n".join(phrases_to_check)
    return phrases_to_check