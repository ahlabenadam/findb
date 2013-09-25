#!/usr/bin/env python
# -*- conding: utf-8 -*-

import sys
import os
import urllib2
import xml.etree.ElementTree as ET
import time
from fin_db import DB
from symbol import Stock

try:
	os.stat('.debug')
	root=os.environ["PWD"]
except OSError:
	home=os.environ["HOME"]
	root=home + '/src/finance'


dbpath=root + '/1.db'
db = DB(dbpath)

def query_google(list):
	if list.__len__() == 0:
		print "Empty list"
		sys.exit(0)

	tmp=[]
	def add_stock_word(sym):
		tmp.append("stock="+sym)
	
	filter(lambda x: add_stock_word(x), list)
	query= "http://www.google.com/ig/api?" + '&'.join(tmp)

	req = urllib2.Request(url=query)
	f = urllib2.urlopen(req)

	tmpfile = open(tname, 'w')
	tmpfile.write(f.read())
	tmpfile.close()


list=[]
tname='tmp'

stocks = db.get_stocks()
filter(lambda x: list.append(x.name), stocks)

def get_sid(sym):
	for S in stocks:
		if S.get_name()  == sym:
			return S.get_id()

query_google(list)

tmpfile = open(tname, 'r')
tree = ET.parse(tname)
tmpfile.close()
root = tree.getroot()
query=[]
for finance in root.findall('finance'):
	def get_child(element,name):
		child = element.find(name)
		if child is None:
			return None
		else:
			data = child.get('data')
			if data.__len__() == 0:
				return None
			else:
				return data

	symbol = get_child(finance,'symbol')
	avgvol = get_child(finance, 'avg_volume')
	mktcap = get_child(finance, 'market_cap')
	if avgvol is not None  and mktcap is not None:
		volume = get_child(finance, 'volume')
		sopen  = get_child(finance, 'open')
		last   = get_child(finance, 'last')
		high   = get_child(finance, 'high')
		low    = get_child(finance, 'low')
		td_UTC = get_child(finance, 'trade_date_utc')
		cd_UTC = get_child(finance, 'current_date_utc')
		ct_UTC = get_child(finance, 'current_time_utc')

		#cmd="INSERT INTO  data VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % (\
		#symbol, sopen, last, high, low, volume, avgvol, mktcap, td_UTC, cd_UTC, ct_UTC)
		#print cmd
		#query.append(cmd)
		query.append((get_sid(symbol), sopen, last, high, low, volume, avgvol, mktcap, td_UTC, cd_UTC, ct_UTC))
	else:
		print "Symbol " + symbol + " has no data"
	
db.executemany('INSERT INTO data VALUES(?,?,?,?,?,?,?,?,?,?,?)',query)

