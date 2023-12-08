import sys
sys.setrecursionlimit(10**7)
result = []
graph = []
visited = []

dr = [-1, 1 , 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(r,c):
    visited[r][c] = 1

    for i in range(8):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0 <= next_r < row and 0 <= next_c < col and graph[next_r][next_c] == 1 and visited[next_r][next_c] == 0:
            dfs(next_r, next_c)




while True:
    cnt = 0
    col, row = map(int, sys.stdin.readline().split())
    if col == row == 0:
        break

    for i in range(row):
        graph.append(list(map(int, sys.stdin.readline().split())))
        visited.append([0]*col)

    for cur_row in range(row):
        for cur_col in range(col):
            if visited[cur_row][cur_col] == 0 and graph[cur_row][cur_col] == 1:
                dfs(cur_row, cur_col)
                cnt += 1

    result.append(cnt)
    graph.clear()
    visited.clear()

for i in result:
    print(i)