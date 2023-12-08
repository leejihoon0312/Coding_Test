from itertools import permutations
import sys


minimum = 1000000000
row = col = int(input())
graph = []
for _ in range(row):
    graph.append(list(map(int, sys.stdin.readline().split())))

for arr in permutations(range(0, row), row):
    arr = list(arr)
    arr.append(arr[0])
    total = 0
    flag = True
    for i in range(row):
        if graph[arr[i]][arr[i + 1]] == 0:
            flag = False
            break
        total += graph[arr[i]][arr[i + 1]]
        if total > minimum:
            break
    if flag:
        minimum = min(total, minimum)

print(minimum)
