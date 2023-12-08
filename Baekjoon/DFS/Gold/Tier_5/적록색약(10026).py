import sys
sys.setrecursionlimit(10**6)

row = col = int(input())

graph = []
visited = []
result = []
for i in range(row):
    graph.append(list(input()))
    visited.append([0]*col)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, isweird):
    visited[r][c] = 1

    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if not isweird:
            if 0 <= next_r < row and 0 <= next_c < col and graph[r][c] == graph[next_r][next_c] and visited[next_r][next_c] == 0:
                dfs(next_r, next_c, isweird)

        else:
            if graph[r][c] != 'B':
                if 0 <= next_r < row and 0 <= next_c < col and ((graph[next_r][next_c] == 'R') or (graph[next_r][next_c] =='G')) and visited[next_r][next_c] == 0:
                    dfs(next_r, next_c, isweird)

            else:
                if 0 <= next_r < row and 0 <= next_c < col and graph[r][c] == graph[next_r][next_c] and visited[next_r][next_c] == 0:
                    dfs(next_r, next_c, isweird)

cnt = 0
for cur_row in range(row):
    for cur_col in range(col):
        if visited[cur_row][cur_col] == 0:
            dfs(cur_row, cur_col, False)
            cnt += 1

result.append(cnt)
visited.clear()
for i in range(row):
    visited.append([0]*col)

cnt = 0
for cur_row in range(row):
    for cur_col in range(col):
        if visited[cur_row][cur_col] == 0:
            dfs(cur_row, cur_col, True)
            cnt += 1
result.append(cnt)

for i in result:
    print(i, end = " ")
