from collections import deque, defaultdict
import sys

vertex, edge, start = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
cnt = 1
visited = {}
for _ in range(edge):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, vertex + 1):
    graph[i].sort()
    graph[i].reverse()


def bfs(start_v):
    q = deque()
    global cnt
    q.append(start_v)
    visited[start_v] = cnt

    while q:
        cur_v = q.popleft()

        for next_v in graph[cur_v]:
            if next_v not in visited:
                cnt += 1
                visited[next_v] = cnt
                q.append(next_v)


bfs(start)

for i in range(1, vertex + 1):
    if i in visited:
        print(visited[i])
    else:
        print(0)
