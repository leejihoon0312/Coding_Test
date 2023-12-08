from collections import deque, defaultdict

vertex = int(input())
edge = int(input())

graph = defaultdict(list)
visited = {}
cnt = 0
for _ in range(edge):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def bfs(start_v):
    q = deque()
    q.append(start_v)
    global cnt
    visited[start_v] = True
    while q:
        cur_v = q.popleft()

        for next_v in graph[cur_v]:
            if next_v not in visited:
                visited[next_v] = True
                cnt += 1
                q.append(next_v)



bfs(1)
print(cnt)