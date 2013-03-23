#!/bin/bash

DB=test
SQLITE="sqlite3 $DB"
SYMBOL=$1

$SQLITE 'CREATE TABLE if NOT EXISTS stock(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE);'
$SQLITE 'CREATE TABLE if NOT EXISTS watch(id INTEGER, watch INTEGER NOT NULL);'
CMD="INSERT INTO stock(id, name) values(NULL, \"$1\");"
 $SQLITE "$CMD"
if [ $? -ne 0 ];then
	echo "Unable to add stock to the list"
	exit 1
fi
#$SQLITE "INSERT INTO watch(id,watch) values(
