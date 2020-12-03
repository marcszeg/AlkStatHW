n = 3 #int(input())

m = []
#m = [int(v) for v in input().split()]
m = [3, 3, 3]
max_m = max(m)


a = [[0 for i in range(max_m)] for j in range(n)]
b = 1

for i in range(n):
    for j in range(m[i]):
        #print(1)
        a[i][j] = b
        b += 1

a = [[-416, -29, -311], [-345, -473, -201], [-376, -142, 33]]

print("a= " + str(a))

negs = [0]*n
pos = [0]*n

for i in range(n):
    for j in range(m[i]):
        if a[i][j] > 0:
            pos[i] += 1
        elif a[i][j] < 0:
            negs[i] += 1

print("pozitívak: " + str(pos))
print("negatívak: " + str(negs))

# idáig jó




c1 = 0
c2 = 0

for i in range(n):
    if i == 0:
        c1 = pos[i]/m[i]
    else:
        c1 *= pos[i]/m[i]

for i in range(n):
    if i == 0:
        c2 = negs[i]/m[i]
    else:
        c2 *= negs[i]/m[i]

print(c1, c2)
c = c1 + c2

print(c)