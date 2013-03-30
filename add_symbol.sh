#!/bin/bash

SYM="stock_$1"
DB=$2

echo "INSERT INTO  stock VALUES(NULL, \"$SYM\", NULL, 1, 1);"
