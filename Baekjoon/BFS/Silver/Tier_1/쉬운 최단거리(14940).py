from collections import deque
import sys

row, col = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
visited = [[0] * col for _ in range(row)]
start_r = start_c = 0

for i in range(row):
    for j in range(col):
        if graph[i][j] == 2:
            start_r = i
            start_c = j
            break

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    q = deque()
    q.append((r, c, 0))
    visited[r][c] = 1
    graph[r][c] = 0
    while q:
        cur_r, cur_c, dist = q.popleft()

        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row and 0 <= next_c < col and visited[next_r][next_c] == 0 and graph[next_r][next_c] != 0:
                visited[next_r][next_c] = 1
                graph[next_r][next_c] = dist + 1
                q.append((next_r, next_c, dist + 1))


bfs(start_r, start_c)

for i in range(row):
    for j in range(col):
        if graph[i][j] == 1 and visited[i][j] == 0:
            print(-1, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
