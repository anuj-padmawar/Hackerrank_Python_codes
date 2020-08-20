# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
x=int(input())
for i in range (x):
    k=input()
    print (bool(re.match(r'^[+-]?\d*?\.{1}\d+$',k)))
