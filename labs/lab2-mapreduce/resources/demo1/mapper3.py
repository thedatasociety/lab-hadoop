import sys

for index, line in enumerate(sys.stdin):
    line = line.strip()
    words = line.split(',')

    # skiping header
    if index  > 0:
        print("{}\t{}".format(words[int(sys.argv[1])], 1))