#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import gzip # because the html using gzip
import io

headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
    "Accept-Encoding": "gzip"
    }
    
req = urllib2.Request('http://finance.sina.com.cn/', headers=headers)

r2 = urllib2.urlopen(req).read()
bi = io.BytesIO(r2)
gf = gzip.GzipFile(fileobj=bi, mode='rb')

soup = BeautifulSoup(gf.read())
h3 = soup.body.find_all('h3')

for i in range(len(h3)):
    print i+1
    print h3[i].a.get('href')
    try:
        print h3[i].a.string.encode('utf-8')
    except:
        x = [s for s in h3[i].a.stripped_strings]
        
        print x[0].encode('utf-8')+x[1].encode('utf-8')
    


