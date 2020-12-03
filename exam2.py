solve=lambda N,K : 1.0-(N-K)*(N-K-1)/(N*(N-1))

n,k=[int(v) for v in input().split()]
a=solve(n,k)
b=2*0.25+3*0.25+4*0.25+5*0.25

print(a*b+(1-a)*1)