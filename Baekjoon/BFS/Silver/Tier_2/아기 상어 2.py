from collections import deque
import sys

row, col = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
visited = [[0] * col for _ in range(row)]

q = deque()

for cur_row in range(row):
    for cur_col in range(col):
        if visited[cur_row][cur_col] == 0 and graph[cur_row][cur_col] == 1:
            q.append((cur_row, cur_col))
            visited[cur_row][cur_col] = 1

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]


def bfs(q):
    while q:
        cur_r, cur_c = q.popleft()

        for i in range(8):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row and 0 <= next_c < col and visited[next_r][next_c] == 0 and graph[next_r][next_c] == 0:
                q.append((next_r, next_c))
                graph[next_r][next_c] = graph[cur_r][cur_c] + 1


bfs(q)
maximum = 0
for i in graph:
    maximum = max(max(i), maximum)

print(maximum - 1)
