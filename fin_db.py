import sqlite3
from symbol import Stock

#__all__ = ["Fin_db"]

#VAL=0
#DBNAME=""

class DB:
	__dbname__ = None
	__conn__   = None
	__cursor__ = None
	__stlist__ = None

	def __init__(self, dbname):
		self.__dbname__ = dbname	
		self.__conn__ = sqlite3.connect(self.__dbname__)
		self.__cursor__ = self.__conn__.cursor()
		self.__cursor__.execute("PRAGMA foreign_keys = ON")

	def get_stocks(self):
		if ( self.__stlist__ == None) :
			self.__stlist__=[]
			res = self.__cursor__.execute("select * from stock")
			r = res.fetchall()
			for record in r:
				s = Stock(record[1][6:], record[0])
				self.__stlist__.append(s)

		return self.__stlist__

	def execute(self, queries):
		for q in queries:
			self.__cursor__.execute(q)
		self.__conn__.commit()
