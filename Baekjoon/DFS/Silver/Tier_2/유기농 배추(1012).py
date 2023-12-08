import sys
sys.setrecursionlimit(10**4)
times = int(input())
result = []
# 상하좌우 이동
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    visited[r][c] = 1

    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0 <= next_r < row and 0 <= next_c < col and graph[next_r][next_c] == 1 and visited[next_r][next_c] == 0:
            dfs(next_r, next_c)


for _ in range(times):
    col, row, location = map(int, input().split())
    graph = [[0] * col for _ in range(row)]
    visited = [[0] * col for _ in range(row)]
    cnt = 0
    for _ in range(location):
        g_col, g_row = map(int, input().split())
        graph[g_row][g_col] = 1

    for cur_row in range(row):
        for cur_col in range(col):
            if visited[cur_row][cur_col] == 0 and graph[cur_row][cur_col] == 1:
                dfs(cur_row, cur_col)
                cnt += 1
    result.append(cnt)


for i in result:
    print(i)
