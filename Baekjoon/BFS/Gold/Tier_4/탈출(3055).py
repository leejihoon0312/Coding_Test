from collections import deque

import sys

row, col = map(int, sys.stdin.readline().split())
graph = []
visited_w = []
visited_b = []
cave_row = 0
cave_col = 0
start_row = 0
start_col = 0
q = deque()
for i in range(row):
    visited_w.append([0] * col)
    visited_b.append([0] * col)

for i in range(row):
    ls = list(sys.stdin.readline().strip())
    if 'D' in ls:
        cave_row = i
        cave_col = ls.index('D')
    if 'S' in ls:
        start_row = i
        start_col = ls.index('S')
    for j in range(col):
        if ls[j] == '*':
            q.append((i, j, 'w', 0))
            visited_w[i][j] = 1
    graph.append(ls)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c, who):
    q.append((r, c, who, 0))
    visited_b[r][c] = 1
    graph[r][c] = '.'

    while q:
        cur_r, cur_c, cur_who, cur_dist = q.popleft()
        if (cur_r == cave_row) and (cur_c == cave_col) and cur_who == 'biber':
            print(cur_dist)
            exit(0)
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row and 0 <= next_c < col and graph[next_r][next_c] != '*' and graph[next_r][next_c] != 'X':
                if cur_who == 'w' and visited_w[next_r][next_c] == 0:
                    if graph[next_r][next_c] == '.':
                        graph[next_r][next_c] = '*'
                        visited_w[next_r][next_c] = 1
                        q.append((next_r, next_c, cur_who, cur_dist + 1))
                    if graph[next_r][next_c] == 'D':
                        continue
                elif cur_who == 'biber' and visited_b[next_r][next_c] == 0:
                    visited_b[next_r][next_c] = 1
                    q.append((next_r, next_c, cur_who, cur_dist + 1))


bfs(start_row, start_col, 'biber')

print('KAKTUS')
