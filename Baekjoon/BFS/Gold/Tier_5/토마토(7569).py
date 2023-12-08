from collections import deque
import sys

col, row, height = map(int, input().split())
graph = []
visited = []
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]
maximum = 0
for _ in range(height):
    temp = []
    temp_visited = []
    for _ in range(row):
        temp.append(list(map(int, sys.stdin.readline().split())))
        temp_visited.append([0] * col)

    visited.append(temp_visited)
    graph.append(temp)

q = deque()
for i in range(height):
    for j in range(row):
        for k in range(col):
            if graph[i][j][k] == 1:
                q.append((i, j, k))
                visited[i][j][k] = 1
                graph[i][j][k] = 0


def bfs():
    global maximum
    while q:
        cur_h, cur_r, cur_c = q.popleft()

        if graph[cur_h][cur_r][cur_c] > maximum:
            maximum = graph[cur_h][cur_r][cur_c]

        for i in range(6):
            next_h = cur_h + dh[i]
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]

            if 0 <= next_h < height and 0 <= next_r < row and 0 <= next_c < col and visited[next_h][next_r][next_c] == 0 and graph[next_h][next_r][next_c] == 0:
                visited[next_h][next_r][next_c] = 1
                graph[next_h][next_r][next_c] = graph[cur_h][cur_r][cur_c] + 1
                q.append((next_h, next_r, next_c))


bfs()


for i in range(height):
    for j in range(row):
        for k in range(col):
            if graph[i][j][k] == 0 and visited[i][j][k] == 0:
                print(-1)
                exit(0)


print(maximum)
