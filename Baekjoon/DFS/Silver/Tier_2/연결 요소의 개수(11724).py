from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 7)
vertex, edge = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
visited = {}
cnt = 0
for i in range(edge):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def dfs(start_v):
    visited[start_v] = True

    for next_v in graph[start_v]:
        if next_v not in visited:
            dfs(next_v)


for i in range(1, vertex+1):
    if i not in visited:
        dfs(i)
        cnt += 1
print(cnt)
