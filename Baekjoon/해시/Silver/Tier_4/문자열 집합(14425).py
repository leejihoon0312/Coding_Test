import sys
from collections import Counter
N, M = map(int, sys.stdin.readline().split())

a = []
b = []
result = 0
for _ in range(N):
    a.append(sys.stdin.readline().strip())

for _ in range(M):
    b.append(sys.stdin.readline().strip())
ca = Counter(a)
cb = Counter(b)
ls = list(ca & cb)
for i in ls:

    if i in dict(cb):
        result += dict(cb)[i]

print(result)