

import sys

sys.setrecursionlimit(10 ** 6)
row, col = map(int, sys.stdin.readline().split())
graph = []
for i in range(row):
    graph.append(list(map(int, input())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    graph[r][c] = 1

    if r == row-1:
        print("YES")
        exit(0)

    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0 <= next_r < row and 0 <= next_c < col and graph[next_r][next_c] == 0:
            dfs(next_r, next_c)


for cur_row in range(1):
    for cur_col in range(col):
        if graph[cur_row][cur_col] == 0:
            dfs(cur_row, cur_col)
print("NO")
