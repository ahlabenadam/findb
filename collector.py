#!/usr/bin/env python
import xml.etree.ElementTree as ET
import urllib2
import sys
import os
import sqlite3



home=os.environ['HOME']
root=home + '/src/finance'

dbpath=root + '/stock.db'
slist=root + '/stock_list'

def update_db(symbol, tdate, open, last ):
	conn = sqlite3.connect(dbpath)
	cursor = conn.cursor()
	sql = """
	create table if not exists """ + symbol + """
	(date text, open num, close num)
	"""
	cursor.execute(sql)
	cursor.executemany('insert into '+symbol+' values (?,?,?)', [(tdate, open, last)])
	conn.commit()


def open_last(element):
	def get_child(element,name):
		child = element.find(name)
		if child is None:
			return "undefined"
		else:
			return child.get('data')

	sopen = get_child(element, 'open')
	slast = get_child(element, 'last')
	stdate = get_child(element,'trade_date_utc')
	
	return sopen, slast, stdate


def symbol_get_exch_data(symbol):
	string ="http://www.google.com/ig/api?stock=" + symbol
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

	sym_open, sym_last, sym_tdate  = open_last(finance)
	update_db(symbol, sym_tdate, sym_open, sym_last)


slist = open(slist, 'r')

for symbol in slist:
	symbol=symbol.strip().rstrip()
	symbol_get_exch_data(symbol)

