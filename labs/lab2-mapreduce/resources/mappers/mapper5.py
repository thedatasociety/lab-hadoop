#!/usr/bin/env python

import sys

for index, line in enumerate(sys.stdin):
    line = line.strip()
    words = line.split(',')

    # skiping header
    if index  > 0:
        print("total,{}".format(words[1]))