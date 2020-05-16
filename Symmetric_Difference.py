# Enter your code here. Read input from STDIN. Print output to STDOUT


n=int(input())
X=set(map(int, input().split()))
m=int(input())
Y=set(map(int, input().split()))
Z= (X.difference(Y)).union(Y.difference(X))


for i in sorted(list(Z)):
        print (i)
