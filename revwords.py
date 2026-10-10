import sys
for line in sys.stdin:
    print(' '.join(reversed(line.split())))
