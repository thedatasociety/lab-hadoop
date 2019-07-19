import sys

for line in sys.stdin:
    line = line.strip()    
    print("{0}\t{1}".format(line, 1))