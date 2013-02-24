#!/bin/bash

if [ $# -eq 0 ];then
	echo "Usage: $0 <SYMBOL>"
	exit 1
fi

curl -o - http://www.google.com/ig/api?stock=$1
