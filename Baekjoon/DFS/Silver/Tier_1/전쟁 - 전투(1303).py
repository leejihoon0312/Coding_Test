import sys
sys.setrecursionlimit(10**6)

col, row = map(int, input().split())
graph = []
visited = []
result = {}
for i in range(row):
    graph.append(list(input()))
    visited.append([0]*col)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r,c, color):
    visited[r][c] = 1
    global cnt

    for i in range(4):
         next_r = r + dr[i]
         next_c = c + dc[i]
         if 0 <= next_r < row and 0 <= next_c < col and visited[next_r][next_c] == 0 and graph[next_r][next_c] == color:
             cnt += 1
             dfs(next_r, next_c, color)


result["W"] = 0
result['B'] = 0
for cur_row in range(row):
    for cur_col in range(col):
        if visited[cur_row][cur_col] == 0:
            cnt = 1
            color = graph[cur_row][cur_col]
            dfs(cur_row, cur_col, color)

            result[color] += cnt**2

print(result["W"], end= " ")
print(result["B"])