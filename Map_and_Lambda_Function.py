cube = lambda x: pow(x,3)# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    x=[0,1]
    for i in range(2,n):
        x.append(x[i-2] + x[i-1])
    return(x[0:n])

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
