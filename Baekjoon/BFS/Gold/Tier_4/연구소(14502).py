from collections import deque
from itertools import combinations

import sys

row, col = map(int, input().split())
graph = []
visited = []
space = []
virus = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
virus_cnt = 0
wall_cnt = 3
safe_cnt = 0
for _ in range(row):
    graph.append(list(map(int, sys.stdin.readline().split())))
    visited.append([0] * col)

for i in range(row):
    for j in range(col):
        if graph[i][j] == 0:
            space.append((i, j))
        if graph[i][j] == 2:
            virus_cnt += 1
            virus.append((i, j))
        if graph[i][j] == 1:
            wall_cnt += 1


def bfs(queue):
    global cnt
    while queue:
        cur_r, cur_c = queue.popleft()

        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row and 0 <= next_c < col and visited[next_r][next_c] == 0 and graph[next_r][next_c] == 0:
                visited[next_r][next_c] = 1
                cnt += 1
                queue.append((next_r, next_c))


q = deque()
for location in list(combinations(space, 3)):

    for _ in range(row):
        visited.append([0] * col)

    cnt = 0
    for i in range(3):
        r, c = location[i]
        graph[r][c] = 1

    for j in virus:
        q.append(j)

    bfs(q)

    safe_cnt = max(safe_cnt, (row * col) - wall_cnt - virus_cnt - cnt)

    for i in range(3):
        r, c = location[i]
        graph[r][c] = 0

    visited.clear()

print(safe_cnt)
