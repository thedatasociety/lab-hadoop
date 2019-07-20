#!/usr/bin/env python

import sys

for index, line in enumerate(sys.stdin):
    line = line.strip()
    words = line.split(',')

    # skiping header
    if index  > 0:
        print("{},{}".format(words[1], 1))