import numpy as np

def solve(M):

    if M<2:
	    return 0
    if M>365:
	    return 1
    return 1.0-np.prod(1.0 - np.array(range(0,M))/365.0)

def min_p(P):
    i = 0
    for i in range(365):
        a=solve(i)
        if a > P:
            break
    
    return i

P = float(input())
print(min_p(P))


