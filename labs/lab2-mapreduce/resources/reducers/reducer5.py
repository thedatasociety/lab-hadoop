#!/usr/bin/env python

import sys

if len(sys.argv) > 1:
    separator = sys.argv[1]
else:
    separator = '\t'

for line in sys.stdin:
    line = line.strip()
    parts = line.split(separator)
    key = parts[0]
    values = parts[1:len(parts)]
    values = map(int, values)

    print( "{0}{1}{2}".format(key, separator, sum(values)) )        