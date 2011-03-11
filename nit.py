# -*- coding: utf-8 -*-

import os,sys
import re
from urllib2 import build_opener
import urllib2
import random
import time


def usage():
    '''
    使用方法
    '''
    how_to_use="使用方法:\nhome()方法展示主页\nshow_list()方法展示指定版块"
    print how_to_use

def show_list(fid):
    opener = build_opener()
    a_link="http://bbs.ngacn.cc/thread.php?fid=%s" %fid
    try:
        page=opener.open(a_link).read().decode('gbk').encode('utf-8')
        links = re.findall(r"<a href=.read\.php\?tid=(\d{7})\&\_fp=1.\s+id.*>(.*?)</a>",page)
        for i in links:
            print "%s|%s" %(i[0],i[1])
    except ValueError:
        print " value error"
        raise
    except urllib2.HTTPError:
        # print ""  
        raise     
                
def show_page(fid):
    opener = build_opener()
    a_link='http://bbs.ngacn.cc/read.php?tid=%s' %fid
    try:
        page=opener.open(a_link).read().decode('gbk').encode('utf-8') 
        contents = re.findall(r"<span\s+id=.(postcontent\d)'\s+class=\'postcontent ubbcode\'>(.*?)</span>",page)
        for i in contents:
            print "%s|%s" %(i[0],i[1])
    except ValueError:
        print "error"
        # raise       
def preview_page():
    pass

def home():
    opener = build_opener()
    url = 'http://bbs.ngacn.cc/'
    page = opener.open(url).read().decode('gbk').encode('utf-8')
    links = re.findall(r"<a href='thread\.php\?fid=(.*?)'>(.*?)</a>",page)
    for i in links:
        a=random.randint(1000000000,9999999999)
        print "%s|%s|%d"%(i[0],i[1],a)

if __name__ == '__main__' :
    usage()
    time.sleep(5)
    home()
