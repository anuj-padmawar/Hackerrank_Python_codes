# Enter your code here. Read input from STDIN. Print output to STDOUT

a,b= (int(input()), int(input()))

x=divmod(a,b)
print(*x,sep='\n')
print(x)

