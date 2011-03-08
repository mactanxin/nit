# -*- coding: utf-8 -*-

import os,sys
import re
from urllib2 import build_opener
import random

def show_list(fid,page_type="fid"):
    if page_type == "fid":
        a_link="http://bbs.ngacn.cc/thread.php?fid=%s" %fid
    else:
        a_link='http://bbs.ngacn.cc/read.php?tid=%s' %fid
    try:
        opener = build_opener()
        page=opener.open(a_link).read()        
    pass
def preview_page():
    pass

def home():
    opener = build_opener()
    url = 'http://bbs.ngacn.cc/'
    page = opener.open(url).read()
    links = re.findall(r'<a href=.thread.*?</a>', page)
    for i in links:
        i=i.replace('a href=\'thread.php?','').replace('</a>','').replace('<','').replace('>','').decode('gbk').encode('utf-8')
        data = i.split('\'')
        # i = re.findall(r'fid=(\d+).*>(.*)</a>',i)
        a=random.randint(1000000000,9999999999)
        print "%s|%s|%d"%(data[0],data[1],a)
# print '\n'.join(links)
# print links

if __name__ == '__main__' :
    home()
