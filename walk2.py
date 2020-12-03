from math import comb

m=int(input())

if m % 2 != 0:
    print(0)
else:
    k=int(m/2)
    p=(1/(4**m))*(comb(m,k)**2)
    print(p)