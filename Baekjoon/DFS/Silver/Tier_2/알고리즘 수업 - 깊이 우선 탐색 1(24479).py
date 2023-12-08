import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
vertex, edge, start = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
visited = {}
result = {}
count = 1
for _ in range(edge):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, edge + 1):
    graph[i].sort()


def dfs(start_v):
    visited[start_v] = True
    global count
    result[start_v] = count
    for next_v in graph[start_v]:
        if next_v not in visited:
            count += 1
            dfs(next_v)


dfs(start)

for cur_v in range(1, vertex + 1):
    if cur_v not in result:
        print(0)
    else:
        print(result[cur_v])
