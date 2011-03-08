# -*- coding: utf-8 -*-

import os,sys
import re
from urllib2 import build_opener
import random

def show(fid,page_type="fid"):
    opener = build_opener()
    if page_type == "fid":
        a_link="http://bbs.ngacn.cc/thread.php?fid=%s" %fid
        try:
            page=opener.open(a_link).read()
            page=page.decode('gbk').encode('utf-8') 
            links=re.findall(r'<a href=.read\.php\?tid=\d{7}\&\_fp=1.\s+id.*</a>', page)
            for i in links:
                i = re.findall(r'tid=(\d+).*>(.*)</a>',i)
                data=i[0]
                print "%s|%s" %(data[0],data[1])
        except:
            print "error"
            pass        
    else :
        a_link='http://bbs.ngacn.cc/read.php?tid=%s' %fid
        try:
            print "start"
            page=opener.open(a_link).read() 
            for i in contents:
                i = i.replace('<span id=\'',"").replace("</span>","").replace("\' class='postcontent ubbcode\'","").replace("<br/>","|")
                k = re.sub(r'\[.*\]','',i)       
                print k
        except:
            print "error"
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
