#!/usr/bin/env python
import sys
import os
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

	
stocks = db.get_stocks()

for s in stocks:
	query=[]
	time.sleep(10)
	s.update()
	cmd="INSERT INTO  data VALUES(%d, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % (\
    s.get_id(), s.sopen, s.last, s.high, s.low, s.volume, s.avgvol, s.mktcap, s.td_UTC, s.cd_UTC, s.ct_UTC\
	)
	query.append(cmd)
	db.execute(query)


