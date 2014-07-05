# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

stock_instrument = '600064' # type the stock instrument you want to get

if int(stock_instrument[0])==6:
    stock_q = 'sh'+stock_instrument
else:
    stock_q = 'sz'+stock_instrument

r = requests.get('http://hq.sinajs.cn/list='+stock_q)

data = BeautifulSoup(r.text).p.string.encode('utf-8') # this is quite important, because the raw data is GBK 
info = data[21:-3].split(',')

stock_datas = {
    'name': info[0],
    'today_open': info[1],
    'yesterday_close': info[2],
    'price_now': info[3],
    'price_high': info[4],
    'price_low': info[5],
    'buy_1': info[6],
    'sell_1': info[7],
    'volume': info[8],
    'volume_yuan': info[9],
    'buy_1_gu': info[10],
    'buy_1_yuan': info[11],
    'buy_2_gu': info[12],
    'buy_2_yuan': info[13],
    'buy_3_gu': info[14],
    'buy_3_yuan': info[15],
    'buy_4_gu': info[16],
    'buy_4_yuan': info[17],
    'buy_5_gu': info[18],
    'buy_5_yuan': info[19],
    'sell_1_gu': info[20],
    'sell_1_yuan': info[21],
    'sell_2_gu': info[22],
    'sell_2_yuan': info[23],
    'sell_3_gu': info[24],
    'sell_3_yuan': info[25],
    'sell_4_gu': info[26],
    'sell_4_yuan': info[27],
    'sell_5_gu': info[28],
    'sell_5_yuan': info[29],
    'date': info[30],
    'time': info[31]
}
print '名称'+' '*10+stock_datas['name']
print '开盘'+' '*10+stock_datas['today_open']
print '当前'+' '*10+stock_datas['price_now']
print '最高'+' '*10+stock_datas['price_high']
print '最低'+' '*10+stock_datas['price_low']
print '昨收'+' '*10+stock_datas['yesterday_close']
variaty = (float(stock_datas['price_now'])/float(stock_datas['yesterday_close'])-1)*100
print '涨跌'+' '*10+str(round(variaty,2))+'%'
print stock_datas['date']
print stock_datas['time']
