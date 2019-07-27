#!/usr/bin/env python

import sys
from itertools import groupby
from operator import itemgetter

pairs = []
separator = "\t"

try:
    separator = sys.argv[1]
except:
    pass

for line in sys.stdin:
    line = line.strip()
    key, value = line.split(separator)
    pairs.append((key, value))

sorter = sorted(pairs, key=itemgetter(0))
grouper = groupby(sorter, key=itemgetter(0))

res = {k: list(map(itemgetter(1), v)) for k, v in grouper}

for pair in res:
    values = ''
    print("{0}{1}{2}".format(pair, separator, separator.join([item for item in res[pair]])))