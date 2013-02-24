#!/bin/bash

if  [ $# -eq 0 ];then
	echo "usage: $0 <SYMBOL>"
	exit 1
fi

#curl -o - "http://query.yahooapis.com/v1/public/yql?q=select%20finance.open%2Cfinance.last%20%20from%20google.igoogle.stock%20where%20stock%3D'$1'%3B&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
curl -o - "http://query.yahooapis.com/v1/public/yql?q=select%20finance.open%2Cfinance.last%2Cfinance.trade_date_utc%20%20from%20google.igoogle.stock%20where%20stock%3D'$1'%3B&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
