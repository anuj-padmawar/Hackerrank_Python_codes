import numpy as np
N,M,P= map(int,raw_input().split())
A= np.array([ map(int,raw_input().split()) for i in range(N)] )
B= np.array([ map(int,raw_input().split()) for i in range(M)] )
print np.concatenate((A,B),axis =0)
