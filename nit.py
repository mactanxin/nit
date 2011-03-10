# -*- coding: utf-8 -*-

import os,sys
import re
from urllib2 import build_opener
import urllib2
import random

def show(fid,page_type="fid"):
    opener = build_opener()
    if page_type == "fid":
        a_link="http://bbs.ngacn.cc/thread.php?fid=%s" %fid
        try:
            page=opener.open(a_link).read().decode('gbk').encode('utf-8')
            links=re.findall(r'<a href=.read\.php\?tid=\d{7}\&\_fp=1.\s+id.*</a>', page)
            for i in links:
                i = re.findall(r'tid=(\d+).*>(.*)</a>',i)
                data=i[0]
                print "%s|%s" %(data[0],data[1])
        except ValueError:
            print " value error"
            raise
        except urllib2.HTTPError:
            # print ""  
            raise     
                    
    else :
        a_link='http://bbs.ngacn.cc/read.php?tid=%s' %fid
        try:
            page=opener.open(a_link).read().decode('gbk').encode('utf-8') 
            contents = re.findall(r'<span.id=.postcontent.*?</span>',page)
            for i in contents:
                i = i.replace('<span id=\'',"").replace("</span>","").replace("\' class='postcontent ubbcode\'","").replace("<br/>","|")
                k = re.sub(r'\[.*\]','',i)       
                print k
        except ValueError:
            print "error"
            # raise       
def preview_page():
    pass

def home():
    opener = build_opener()
    url = 'http://bbs.ngacn.cc/'
    page = opener.open(url).read().decode('gbk').encode('utf-8')
    links = re.findall(r'<a href=.thread.*?</a>', page)
    for i in links:
        data = re.findall(r"<a href='thread\.php\?(fid=.*?)'>(.*?)</a>",i)[0]
        a=random.randint(1000000000,9999999999)
        print "%s|%s|%d"%(data[0],data[1],a)

if __name__ == '__main__' :
    home()
