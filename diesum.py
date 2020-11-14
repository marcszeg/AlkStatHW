n=int(input())

pre=[0]*((6*n)+1)
p=1.0/6.0**n

def dicethrow(n,N):
    for j in range(1,7):
        if n > 1:
            k = j + dicethrow(n-1,N)
            if n == N:
                pre[k]+=p
            else:
                return k
        else:
            return j


dicethrow(n,n)

for i in range(len(pre)):
    print(pre[i])