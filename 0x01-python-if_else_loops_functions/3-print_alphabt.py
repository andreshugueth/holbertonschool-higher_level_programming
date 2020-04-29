#!/usr/bin/python3
for l in range(97, 123):
    if l == 101 or l == 113:
        continue
    print("{:c}".format(l), end='')
