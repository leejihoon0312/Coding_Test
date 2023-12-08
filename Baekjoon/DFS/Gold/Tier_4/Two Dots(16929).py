import sys

row, col = map(int, sys.stdin.readline().split())
graph = []
visited = [[0] * col for _ in range(row)]
for _ in range(row):
    graph.append(list(sys.stdin.readline().strip()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, find_str, move):
    visited[r][c] = move

    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0 <= next_r < row and 0 <= next_c < col and graph[next_r][next_c] == find_str:

            if visited[next_r][next_c] != 0 and abs(move - visited[next_r][next_c]) >= 3:
                print('Yes')
                exit(0)

            if visited[next_r][next_c] == 0:
                dfs(next_r, next_c, find_str, move + 1)


for i in range(row):
    for j in range(col):
        if visited[i][j] == 0:
            dfs(i, j, graph[i][j], 1)

print('No')
