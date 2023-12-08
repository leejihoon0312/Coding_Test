import sys
sys.setrecursionlimit(10**6)

row, col = map(int, input().split())

graph = []
visited = []
result = {}

for i in range(row):
    visited.append([0]*col)
    graph.append(list(input()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r,c):
    visited[r][c] = 1
    global lamb, wolf
    if graph[r][c] == 'o':
        lamb += 1
    elif graph[r][c] == 'v':
        wolf += 1

    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0<= next_r < row and 0<= next_c < col and graph[next_r][next_c] != '#' and visited[next_r][next_c] ==0:
            dfs(next_r, next_c)
result["lamb"] = 0
result["wolf"] = 0
for cur_row in range(row):
    for cur_col in range(col):
        if graph[cur_row][cur_col] != '#' and visited[cur_row][cur_col] == 0:
            wolf = lamb = 0
            dfs(cur_row, cur_col)
            if wolf>=lamb:
                result["wolf"] += wolf
            else:
                result["lamb"] += lamb

for i in result.keys():
    print(result[i], end = " ")