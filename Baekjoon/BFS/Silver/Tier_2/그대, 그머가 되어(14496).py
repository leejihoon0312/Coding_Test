from collections import deque, defaultdict
import sys

start, end = map(int, sys.stdin.readline().split())
vertex, edge = map(int, sys.stdin.readline().split())

graph = defaultdict(list)
visited = {}
for _ in range(edge):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def bfs(start_v):
    q = deque()
    q.append((start_v, 0))
    visited[start_v] = True
    global end
    while q:
        cur_v, dist = q.popleft()

        if cur_v == end:
            print(dist)
            exit(0)

        for next_v in graph[cur_v]:
            if next_v not in visited:
                q.append((next_v, dist+1))
                visited[next_v] = True



bfs(start)
print(-1)