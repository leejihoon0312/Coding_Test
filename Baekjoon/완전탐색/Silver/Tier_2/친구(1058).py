from collections import deque, defaultdict
import sys

vertex = int(input())
graph = defaultdict(list)
count = 2
maximum = 0
for i in range(vertex):
    ls = list(sys.stdin.readline().strip())
    for j in range(len(ls)):
        if ls[j] == "Y":
            graph[i].append(j)


def bfs(v, cnt):
    q = deque()
    q.append((v, cnt))
    visited[v] = 1
    global num
    while q:
        cur_v, cur_cnt = q.popleft()

        for next_v in graph[cur_v]:
            if next_v not in visited and cur_cnt - 1 >= 0:
                visited[next_v] = 1
                num += 1
                q.append((next_v, cur_cnt - 1))


for i in range(vertex):
    visited = {}
    num = 0
    bfs(i, count)
    maximum = max(maximum, num)
    visited.clear()

print(maximum)
