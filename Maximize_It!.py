# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
K,M=map(int,input().split())
X=[]
for _ in range(K):
    list1=map(int,input().split()[1:])
    X.append(map(lambda x:x*x%M,list1))

max1=0
max1=max(map(lambda x:sum(x)%M,itertools.product(*X)))
print(max1)

