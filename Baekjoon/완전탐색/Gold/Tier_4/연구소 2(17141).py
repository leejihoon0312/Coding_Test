from itertools import combinations
from collections import deque
import sys, copy

N, virus_cnt = map(int, input().split())
able = []
row = col = N
graph = []
min_dist = 10**10
empty_space = 0
result = []
for i in range(row):
    ls = list(map(int, sys.stdin.readline().split()))
    for j in range(len(ls)):
        if ls[j] == 2:
            able.append((i, j))
            empty_space += 1
        elif ls[j] == 0:
            empty_space += 1

    graph.append(ls)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1 ,1]

def bfs(queue):
    global min_dist, spread
    dist = 0
    while queue:
        cur_r , cur_c, cur_dist = queue.popleft()

        if cur_dist > dist:
            dist = cur_dist

        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0<=next_r<row and 0<=next_c<col and visited[next_r][next_c] == 0 and copy_graph[next_r][next_c] != 1:
                visited[next_r][next_c] = 1
                spread += 1
                copy_graph[next_r][next_c] = "#"
                q.append((next_r, next_c, cur_dist+1))
    return dist

for location in list(combinations(able, virus_cnt)):
    visited = [[0] * col for _ in range(row)]
    copy_graph = copy.deepcopy(graph)
    spread = 0
    q = deque()
    for r,c in location:
        visited[r][c] = 1
        spread += 1
        q.append((r, c, 0))

    spread_time = bfs(q)

    if spread == empty_space:
        result.append(True)
        min_dist = min(spread_time, min_dist)
    else:
        result.append(False)
    visited.clear()

if any(result):
    print(min_dist)
else:
    print(-1)