from itertools import combinations
import sys

size = int(input())
arr = list(map(int, sys.stdin.readline().split()))
visited = {}

for i in range(1, size+1):
    c = combinations(arr,i)

    for ls in c:
        total = 0
        for j in range(len(ls)):
            total += ls[j]
        if total not in visited:
            visited[total] = 1

for i in range(1, 100000 * 20+1):
    if i not in visited:
        print(i)
        exit(0)
