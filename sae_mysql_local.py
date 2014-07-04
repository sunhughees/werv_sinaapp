# -*- coding:utf-8 -*-

# first, you should install the local environment
# very easy, just do this:
# pip install sae-python-dev

import os
if 'SERVER_SOFTWARE' not in os.environ:
    from sae._restful_mysql import monkey
    monkey.patch()

# make sure type above codes before import MySQLdb

import MySQLdb

SAE_HOST = 'w.rdc.sae.sina.com.cn'
SAE_PORT = 3307
SAE_USER = '' # your access key
SAE_PASSWD = '' #  your secret key
SAE_DB = 'app_'+'' # your app name 


conn = MySQLdb.connect(host=SAE_HOST,
                       port=3307,
                       user=SAE_USER,
                       passwd=SAE_PASSWD,
                       db=SAE_DB)

cur =conn.cursor()

# now you can start the SQL coding
# for example, creat a users table, and some users

cur.execute('CREATE TABLE users(login VARCHAR(8), uid INT)')
cur.execute("INSERT INTO users VALUES('john', 7000)")
cur.execute("INSERT INTO users VALUES('jane', 7001)")
cur.execute("INSERT INTO users VALUES('jack', 6000)")
cur.execute("INSERT INTO users VALUES('bob', 7100)")

cur.close()

conn.commit() # commit all
conn.close() # don't foget to close the connect
