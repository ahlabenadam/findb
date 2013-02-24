#!/bin/bash

if  [ $# -eq 0 ];then
	echo "usage: $0 <SYMBOL>"
	exit 1
fi

curl -o - "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20google.igoogle.stock%20where%20stock%3D'$1'%3B&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
