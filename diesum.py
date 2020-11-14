from itertools import product

n=int(input())

pre=[0]*((6*n)+1)
p=1.0/6.0**n

numbers = product([1, 2, 3, 4, 5, 6], repeat=n)

throws = list(numbers)

sums=[0]*(6**n)

for i in range(len(sums)):
    thrown = 0
    for j in range(n):
        thrown += throws[i][j]
    sums[i]=thrown

for k in range(len(sums)):
    pre[sums[k]] += p

for l in range(n, len(pre)):
    print(pre[l])