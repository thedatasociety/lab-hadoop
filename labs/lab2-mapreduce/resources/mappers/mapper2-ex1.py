#!/usr/bin/env python

import sys

if len(sys.argv) > 1:
    separator = sys.argv[1]
else:
    separator = ','

if len(sys.argv) > 2:
    column = int(sys.argv[2])
else:
    column = 1



for line in sys.stdin:
    line = line.strip()
    parts = line.split(separator)
    avg = float(parts[column])

    if avg >=29 and avg <= 34:
        print( "avg-29-34{}1".format(separator) )        