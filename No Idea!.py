# Enter your code here. Read input from STDIN. Print output to STDOUT
c,d=(int(i) for i in input().split())
n=map(int, input().strip().split(' '))
a=set(map(int, input().strip().split(' ')))
b=set(map(int, input().strip().split(' ')))
happiness=0
a=set(a)
b=set(b)
for x in n:
        if x in a:
            happiness += 1
        elif x in b:
            happiness -= 1

print(happiness)
