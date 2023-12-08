import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
case = int(input())
graph = defaultdict(list)
visited = {}
result = []


def dfs(start_v, flag):
    visited[start_v] = 1

    if flag:
        if start_v in compare:
            result.append(start_v)
            return
    if not flag:
        compare.append(start_v)

    for next_v in graph[start_v]:
        if next_v not in visited:

            dfs(next_v, flag)


for i in range(case):
    compare = []
    edge = int(input())
    for _ in range(edge - 1):
        p_v, c_v = map(int, sys.stdin.readline().split())
        graph[c_v].append(p_v)
    v1, v2 = map(int, sys.stdin.readline().split())
    dfs(v1, False)
    visited.clear()
    dfs(v2, True)
    visited.clear()
    graph.clear()

for i in result:
    print(i)