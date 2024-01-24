import sys

N = int(input())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)

result = 0
for i in range(N):
    result += (A[i]*B[i])

print(result)