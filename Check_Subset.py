# Enter your code here. Read input from STDIN. Print output to STDOUT


for i in range(int(raw_input())):
    a=int(raw_input()); 
    A=set(raw_input().split())
    b=int(raw_input());
    B=set(raw_input().split())
    print True if B.intersection(A)==A else False
