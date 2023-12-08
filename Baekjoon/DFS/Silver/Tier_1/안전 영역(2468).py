import sys
sys.setrecursionlimit(10**6)
row = col = int(input())
graph = []
visited = []

result = []
for _ in range(row):
    graph.append(list(map(int, input().split())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    visited[r][c] = 1

    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0<= next_r <row and 0<= next_c<col and  visited[next_r][next_c] == 0 and graph[next_r][next_c]>height:
            dfs(next_r, next_c)


for height in range(101):
    cnt = 0
    for _ in range(row):
        visited.append([0] * col)
    for cur_row in range(row):
        for cur_col in range(col):
            if visited[cur_row][cur_col] == 0 and graph[cur_row][cur_col] > height:
                dfs(cur_row, cur_col)
                cnt += 1
    result.append(cnt)
    visited.clear()

print(max(result))