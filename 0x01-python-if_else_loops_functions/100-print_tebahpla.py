#!/usr/bin/python3
count = 0
for n in range(122, 96, -1):
    if count == 0:
        print("{:c}".format(n), end="")
        count = 1
    else:
        print("{:c}".format(n - 32), end="")
        count = 0
