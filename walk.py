from scipy.stats import binom

m=int(input())

if m % 2 != 0:
    print(0)
else:
    k=int(m/2)
    p=binom.pmf(k,m,0.5)
    print(p)