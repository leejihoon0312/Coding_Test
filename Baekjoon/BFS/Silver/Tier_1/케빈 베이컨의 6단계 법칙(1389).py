from collections import deque, defaultdict
import sys

vertex, edge = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
result = {}
visited = {}
for _ in range(edge):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def bfs(start_v):
    q = deque()
    q.append((start_v, 0))
    visited[start_v] = True
    global cnt
    while q:
        cur_v, dist = q.popleft()
        cnt += dist

        for next_v in graph[cur_v]:
            if next_v not in visited:
                visited[next_v] = True
                q.append((next_v, dist + 1))


for v in range(1, vertex + 1):
    cnt = 0

    bfs(v)

    result[v] = cnt
    visited.clear()

vertex_num = 1
minimum = result[1]

for i in range(1, vertex + 1):

    if result[i] < minimum:
        minimum = result[i]
        vertex_num = i

print(vertex_num)
