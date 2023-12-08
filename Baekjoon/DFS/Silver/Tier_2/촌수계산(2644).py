import sys
from collections import defaultdict
node = int(sys.stdin.readline())
n1, n2 = map(int, sys.stdin.readline().split())

edge = int(sys.stdin.readline())
graph = defaultdict(list)
visited = {}
cnt = 0
for i in range(edge):
    parent, child = map(int, sys.stdin.readline().split())
    graph[parent].append(child)
    graph[child].append(parent)


def dfs(start_n, fin_n, count):
    visited[start_n] = True

    if start_n == fin_n:
        print(count)

    for next_n in graph[start_n]:
        if next_n not in visited:
            dfs(next_n, fin_n, count+1)

dfs(n1, n2, cnt)

if n1 not in visited or n2 not in visited:
    print(-1)
