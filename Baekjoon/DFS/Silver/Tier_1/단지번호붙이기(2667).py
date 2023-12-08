import sys
row = col = int(sys.stdin.readline())
graph = []
visited = []
result = []
for _ in range(row):
    graph.append(list(map(int, input())))
    visited.append([0]*col)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    visited[r][c] = 1
    global count
    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0<= next_r <row and 0<= next_c <col and visited[next_r][next_c] ==0 and graph[next_r][next_c] == 1:
            count += 1
            dfs(next_r, next_c)




for cur_row in range(row):
    for cur_col in range(col):
        if visited[cur_row][cur_col] == 0 and graph[cur_row][cur_col] == 1:
            count = 1
            dfs(cur_row, cur_col)
            result.append(count)


result.sort()
print(len(result))
for i in result:
    print(i)