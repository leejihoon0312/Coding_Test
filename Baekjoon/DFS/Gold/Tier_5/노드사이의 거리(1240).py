import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

vertex, pair = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
visited = dict()
result = []
for _ in range(vertex-1):
    v1, v2, dist = map(int, sys.stdin.readline().split())
    graph[v1].append((v2, dist))
    graph[v2].append((v1, dist))


def dfs(start_v, distance):
    visited[start_v] = True

    if start_v == to_v:
        result.append(distance)

    for info in graph[start_v]:
        next_v, weight = info
        if next_v not in visited:
            dfs(next_v, distance+weight)


for _ in range(pair):
    from_v, to_v = map(int, sys.stdin.readline().split())

    dfs(from_v, 0)
    visited.clear()


for i in result:
    print(i)