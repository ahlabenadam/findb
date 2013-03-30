#!/bin/bash

DB=$1
SQLITE=sqlite3
STLIST=$2

if [ ! -e $DB ];then
	$SQLITE  $DB < tables.sql
fi

rm cmd
while read line ;do
	./add_symbol.sh $line | $SQLITE $DB  
	if [ $? -ne 0 ];then
		echo $line
	fi
done < <(cat $STLIST)
