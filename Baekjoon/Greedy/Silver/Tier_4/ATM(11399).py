import sys

N =  int(input())

time = list(map(int, sys.stdin.readline().split()))

time.sort()

for i in range(1, N):
    time[i] += time[i-1]

print(sum(time))