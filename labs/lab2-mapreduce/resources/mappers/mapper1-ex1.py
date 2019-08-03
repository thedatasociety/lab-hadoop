#!/usr/bin/env python

import sys

for index, line in enumerate(sys.stdin):
    line = line.strip()
    words = line.split(' ')

    for word in words:
        if "truth" in word:
            print("truth,1".format(word))
        elif "immediately" in word :
            print("immediately,1".format(word))