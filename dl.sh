#!/bin/bash
# download input file for $1 (year) and $2 (day)
cat cookies.txt | wget -O input.txt --no-cookies --header "Cookie: session=$(</dev/stdin)" https://adventofcode.com/$1/day/$2/input