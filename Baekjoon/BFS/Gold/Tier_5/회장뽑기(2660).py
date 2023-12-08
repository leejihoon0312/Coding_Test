from collections import deque, defaultdict

vertex = int(input())
graph = defaultdict(list)
visited = {}
result = []
minimum = 51
while True:
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    if v1 == v2 == -1:
        break


def bfs(start_v):
    q = deque()
    q.append((start_v, 0))
    visited[start_v] = 1
    dist = 0

    while q:
        cur_v, cur_dist = q.popleft()

        if cur_dist > dist:
            dist = cur_dist

        for next_v in graph[cur_v]:
            if next_v not in visited:
                visited[next_v] = 1
                q.append((next_v, cur_dist + 1))

    return dist


for member in range(1, vertex + 1):
    num = bfs(member)
    if num < minimum:
        minimum = num
        result.clear()
        result.append(member)
    elif num == minimum:
        result.append(member)
    visited.clear()

print(minimum, end=" ")
print(len(result))
for i in result:
    print(i, end=" ")
