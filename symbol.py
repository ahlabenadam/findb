import xml.etree.ElementTree as ET
import urllib2


class Stock:
	def __init__(self, symbol, sid):
		self.name = symbol
		self.dname = "stock__" + symbol
		self.sid = sid

	def get_name(self):
		return self.name

	def dname(self):
		return self.dname

	def get_id(self):
		return self.sid

	def pprint(self):
		print "Symbol: " +  self.name
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

		string ="http://www.google.com/ig/api?stock=" + self.name
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
	
