solve=lambda N,K : 1.0-(N-K)*(N-K-1)/(N*(N-1))

def min_chance(n,p):
    b = int(n)
    i=0
    for i in range(b):
        a=solve(b,i)
        if a>=p:
            break
    return i

n,p=[float(v) for v in input().split()]
print(min_chance(n,p))