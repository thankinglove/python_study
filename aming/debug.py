#!/usr/bin/env python
import sys

sum = 0
for item in range(0, 100, 3):
    sum += item
    print(item, sum)

print(sys.argv[1])