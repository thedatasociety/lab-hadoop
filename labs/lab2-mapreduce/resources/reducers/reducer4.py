#!/usr/bin/env python

from operator import itemgetter
import sys

current_key = None
current_value = 0
key = None
value = 0

values=[]

for line in sys.stdin:
    line = line.strip()
    key,value = line.split(sys.argv[1])
    value = float(value)


    values.append(value)

print( "len{1}{2}".format(current_key, sys.argv[1] , len(values) ) )   
print( "sum{1}{2}".format(current_key, sys.argv[1] , sum(values) ) )
print( "avg{1}{2}".format(current_key, sys.argv[1] , sum(values)/len(values) ) )