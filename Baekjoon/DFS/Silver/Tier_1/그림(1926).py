import sys
sys.setrecursionlimit(10**6)

row, col = map(int, input().split())
graph = []
visited = []
result = []
for i in range(row):
    graph.append(list(map(int, input().split())))
    visited.append([0]*col)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r,c):
    visited[r][c] = 1
    global cnt
    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0<= next_r < row and 0<= next_c <col and graph[next_r][next_c] == 1 and visited[next_r][next_c] ==0:
            cnt += 1
            dfs(next_r, next_c)


for cur_row in range(row):
    for cur_col in range(col):
        if graph[cur_row][cur_col] == 1 and visited[cur_row][cur_col] ==0:
            cnt = 1
            dfs(cur_row, cur_col)
            result.append(cnt)

print(len(result))

if len(result) == 0:
    print(0)
else:
    print(max(result))

