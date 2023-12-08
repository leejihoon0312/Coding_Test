import sys
sys.setrecursionlimit(10**6)

row, col, location = map(int, input().split())
graph = []
visited = []
max = 0


for i in range(row):
    visited.append([0]*col)
    graph.append([0] * col)
for i in range(location):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    visited[r][c] = 1
    global cnt
    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0<= next_r <row and 0<= next_c<col and graph[next_r][next_c] ==1 and visited[next_r][next_c]==0:
            cnt += 1
            dfs(next_r, next_c)





for cur_row in range(row):
    for cur_col in range(col):
        if graph[cur_row][cur_col] == 1 and visited[cur_row][cur_col] == 0:
            cnt = 1
            dfs(cur_row, cur_col)
            if cnt>max:
                max = cnt

print(max)