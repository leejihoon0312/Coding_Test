

from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

vertex, edge = map(int, input().split())
graph = defaultdict(list)
visited = {}
inputs = [0] * (vertex+1)
output = [0] * (vertex+1)
num = 0
for _ in range(edge):
    p_v, c_v = map(int, input().split())
    graph[c_v].append(p_v)



def dfs(start_v):
    visited[start_v] = 1
    global cnt
    for next_v in graph[start_v]:
        if next_v not in visited:
            cnt += 1
            inputs[next_v] += 1
            dfs(next_v)


for v in range(1, vertex+1):
    cnt = 0
    dfs(v)
    output[v] = cnt
    visited.clear()

for v in range(1, vertex+1):
    if inputs[v] >=((vertex+1)/2) or output[v] >=((vertex+1)/2):
        num += 1

print(num)