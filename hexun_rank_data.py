#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import json
import time
import requests
import ast

# this url was got from the http://quote.hexun.com/default.htm#stock -->-- rand.aspx -->-- industryquotecon.aspx
# using the 360 web browser
url_text = 'http://quote.stock.hexun.com/hqzx/industryquotecon.aspx?sorttype=4&page=1&count=150&time=194410'

r = requests.get(url_text)

raw_data = r.text.encode('utf-8')[10:-53]

# this ast method can Safely evaluate an expression node or a Unicode or Latin-1 encoded string containing a Python expression
list_data = ast.literal_eval(raw_data)

m = len(list_data)
n = len(list_data[0])
xx = ''
for i in xrange(m):
    for j in xrange(n):
        xx += str(list_data[i][j])+'|'
    xx += '\n'
print xx



