#!/bin/python3

import math
import os
import random
import re
import sys



n, m = map(int, input().split())
rows = [input() for _ in range(n)]
k = int(input())

for row in sorted(rows, key=lambda row: int(row.split()[k])):
    print(row)
