import sys
for line in sys.stdin:
    sys.stdout.write(line.rstrip("\n").upper() + "\n")
