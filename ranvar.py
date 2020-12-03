import math

v = []
p = []

v = [int(v) for v in input().split()]
p = [float(f) for f in input().split()]

varh_ert = 0

for i in range(len(v)):
    varh_ert += v[i]*p[i]

szoras = 0
seged1 = 0

for j in range(len(v)):
    seged1 += ((v[j]**2) * p[j])

szoras = math.sqrt(seged1 - (varh_ert**2))

print(varh_ert, szoras)