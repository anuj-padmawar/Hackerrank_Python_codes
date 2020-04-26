# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

shoes=int(input())
shoe_size=Counter(map(int, input().split()))
num_customers=int(input())

cost = 0
for _ in range(num_customers):
    size, price=map(int, input().split())
    if shoe_size[size]:
        cost += price
        shoe_size[size] -= 1

print(cost)
