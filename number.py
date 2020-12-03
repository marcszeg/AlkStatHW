a = []
b = []

n,M=[int(g) for g in input().split()]
a=[int(v) for v in input().split()]
b=[int(f) for f in input().split()]

a_neg = 0
a_poz = 0
b_neg = 0
b_poz = 0

for i in range(len(a)):
    if a[i] > 0:
        a_poz += 1
    elif a[i] < 0:
        a_neg += 1

for j in range(len(b)):
    if b[j] > 0:
        b_poz += 1
    elif b[j] < 0:
        b_neg += 1

c = (a_poz/len(a))*(b_poz/len(b)) + (a_neg/len(a))*(b_neg/len(b))

print(c)