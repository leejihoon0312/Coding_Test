from collections import deque, defaultdict
import sys
vertex, node, distance, start = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
visited = {}
cnt = 0
result = []
for _ in range(node):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)


def bfs(start_num):
    q = deque()
    q.append((start_num, 0))
    visited[start_num] = True
    global cnt, distance
    while q:
        cur_num, cnt = q.popleft()

        if cnt == distance:
            result.append(cur_num)
            continue
        for next_v in graph[cur_num]:
            if next_v not in visited and cnt+1<=distance:
                visited[next_v] = True
                q.append((next_v, cnt+1))


bfs(start)
result.sort()
if len(result) ==0:
    print(-1)
else:
    for i in result:
        print(i)
