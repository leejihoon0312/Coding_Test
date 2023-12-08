import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)
node = int(sys.stdin.readline())
graph = defaultdict(list)
visited = {}
previous = {}
for i in range(node - 1):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)


def dfs(start_n, find_n):
    visited[start_n] = True
    if start_n == find_n:
        print(previous[find_n])

    for next_n in graph[start_n]:
        if next_n not in visited:
            previous[next_n] = start_n
            dfs(next_n, find_n)


for i in range(2, node + 1):
    if i not in previous:
        dfs(1, i)
        visited.clear()
    else:
        print(previous[i])
