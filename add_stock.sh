#!/bin/bash


DB=test.db
LIST="st_list"

rm $DB
SQLITE="sqlite3 $DB"
SYMBOL=$1

$SQLITE 'CREATE TABLE if NOT EXISTS st_list(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE);'
$SQLITE 'CREATE TABLE if NOT EXISTS watch(id INTEGER, watch INTEGER NOT NULL);'

while read line;do
	CMD="INSERT INTO st_list(id, name) values(NULL, \"$line\");"
	 $SQLITE "$CMD"
	if [ $? -ne 0 ];then
		echo "Unable to add stock to the list"
		exit 1
	fi

	#sopen, last, high, low, volume, avgvol, mktcap, stdate, cdate, ctime)  values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
	CMD="CREATE TABLE if NOT EXISTS \"$line\"(sopen INTEGER, last INTEGER, high INTEGER, low INTEGER, volume INTEGER, \
		avgvol INTEGER, mktcap INTEGER, stdate TEXT, cdate TEXT, ctime TEXT)"
	$SQLITE "$CMD"
done < <(cat $LIST)

#$SQLITE "INSERT INTO watch(id,watch) values(
$SQLITE 'select * from st_list'
