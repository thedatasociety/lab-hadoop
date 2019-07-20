#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split(' ')

    for word in words:
        word = word.replace(' ','')
        # word = ''.join(e for e in word if e.isalnum())        
        # word = word.lower()
        if word != '':
            print("{}\t{}".format(word, 1))











