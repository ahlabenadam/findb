#!/bin/bash

sym=`echo $1 | tr [a-z] [A-Z]`
SYM="stock_$sym"

echo "INSERT INTO  stock VALUES(NULL, \"$SYM\", NULL, 1, 1);"
