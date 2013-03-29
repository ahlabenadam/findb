#!/usr/bin/env python
import xml.etree.ElementTree as ET
import urllib2
import sys
import os
import sqlite3



home=os.environ['HOME']
root=home + '/src/finance'

dbpath=root + '/test.db'
slist=root + '/st_list'

class Stock:
	def __init__(self, symbol):
		self.symbol = symbol

	def pprint(self):
		print "Symbol: " +  self.symbol
		print "Open: " + self.sopen
		print "Close: " + self.last
		print "High: " + self.high
		print "Low: " + self.low
		print "Volume: " + self.volume
		print "Avgvol: " + self.avgvol
		print "Mktcap: " + self.mktcap
		print "Trade date UTC: " + self.td_UTC
		print "Date UTC: " + self.cd_UTC
		print "Time UTC: " + self.ct_UTC

	
	def update(self):
		def get_child(element,name):
			child = element.find(name)
			if child is None:
				return "undefined"
			else:
				return child.get('data')

		string ="http://www.google.com/ig/api?stock=" + self.symbol
		tname='tmp'
		tmpfile = open(tname, 'w')

		req = urllib2.Request(url=string)
		f = urllib2.urlopen(req)

		tmpfile.write(f.read())
		tmpfile.close()
		tmpfile = open(tname,'r')


		tree = ET.parse(tmpfile)
		tmpfile.close()
		root = tree.getroot()

		finance = root.find('finance')
		if finance is None:
			print "Element not found"
			return

		self.sopen =  get_child(finance, 'open')
		self.last =  get_child(finance, 'last')
		self.high =   get_child(finance, 'high')
		self.low  =   get_child(finance, 'low')
		self.volume  =   get_child(finance, 'volume')
		self.avgvol  =   get_child(finance, 'avg_volume')
		self.mktcap  =   get_child(finance, 'market_cap')
		self.td_UTC = get_child(finance, 'trade_date_utc')
		self.cd_UTC  = get_child(finance, 'current_date_utc')
		self.ct_UTC =  get_child(finance, 'current_time_utc')
	
	
def update_db(s):
	conn = sqlite3.connect(dbpath)
	cursor = conn.cursor()
	cursor.executemany('insert into '+symbol+'(\
	sopen, last, high, low, volume, avgvol, mktcap, stdate, cdate, ctime)  values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
	[(s.sopen, s.last, s.high, s.low, s.volume, s.avgvol, s.mktcap, s.td_UTC, s.cd_UTC, s.ct_UTC)])
	conn.commit()


stocks = open(slist, 'r')

for symbol in stocks:
	symbol=symbol.strip().rstrip()
	s = Stock(symbol)
	s.update()
	update_db(s)

