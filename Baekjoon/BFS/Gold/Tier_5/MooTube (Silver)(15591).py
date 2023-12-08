from collections import deque, defaultdict

vertex, question = map(int, input().split())
graph = defaultdict(list)
visited = {}
result = []
for _ in range(vertex - 1):
    v1, v2, weight = map(int, input().split())
    graph[v1].append((v2, weight))
    graph[v2].append((v1, weight))


def bfs(start_v):
    q = deque()
    q.append(start_v)
    visited[start_v] = 1
    global cnt
    while q:
        cur_v = q.popleft()

        for i in graph[cur_v]:
            next_v, dist = i
            if next_v not in visited and dist >= weight:
                visited[next_v] = 1
                cnt += 1
                q.append(next_v)


for _ in range(question):
    weight, v = map(int, input().split())
    cnt = 0
    bfs(v)
    result.append(cnt)
    visited.clear()

for i in result:
    print(i)
