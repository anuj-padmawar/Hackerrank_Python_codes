# Enter your code here. Read input from STDIN. Print output to STDOUT

N,X=map(int,input().split())
marks=[]
for _ in range(X):
    marks.append(map(float, input().split()))

for i in zip(*marks):
    print(sum(i)/len(i))
