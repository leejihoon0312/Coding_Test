from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 7)
vertex = int(sys.stdin.readline())
graph = defaultdict(list)
visited = {}
maximum = 0
leaf = 0
max_weight = 0
for _ in range(vertex - 1):
    v1, v2, weight = map(int, sys.stdin.readline().split())
    graph[v1].append((v2, weight))
    graph[v2].append((v1, weight))


def dfs(start_v, cur_weight):
    visited[start_v] = 1
    global maximum, leaf
    if cur_weight > maximum:
        maximum = cur_weight
        leaf = start_v

    for i in graph[start_v]:
        next_v, next_weight = i
        if next_v not in visited:
            dfs(next_v, cur_weight + next_weight)


dfs(1, 0)
visited.clear()
maximum = 0
dfs(leaf, 0)

print(maximum)
