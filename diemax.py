from itertools import product

n,M=[int(v) for v in input().split()]

pre=[0]*7
p=1.0/6.0**n

numbers = product([1, 2, 3, 4, 5, 6], repeat=n)

throws = list(numbers)

for i in range(len(throws)):
    pre[max(throws[i])]+=p

print(pre[M])