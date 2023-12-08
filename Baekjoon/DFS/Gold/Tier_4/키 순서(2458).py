from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
vertex, compare = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
visited = {}
result = 0

inputs = [0] * (vertex + 1)
output = [0] * (vertex + 1)

for _ in range(compare):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)


def dfs(start_v):
    visited[start_v] = 1
    global cnt

    for next_v in graph[start_v]:
        if next_v not in visited:
            inputs[next_v] += 1
            cnt += 1
            dfs(next_v)


for v in range(1, vertex + 1):
    cnt = 0
    dfs(v)
    output[v] = cnt
    visited.clear()
for v in range(1, vertex + 1):
    if inputs[v] + output[v] == vertex - 1:
        result += 1

print(result)
