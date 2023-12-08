from collections import deque
import sys

row, col = map(int, input().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(row)]
maximum = -1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    q = deque()
    q.append((r, c, 0))
    visited[r][c] = 1
    global maximum

    while q:
        cur_row, cur_col, dist = q.popleft()
        if dist > maximum:
            maximum = dist

        for i in range(4):
            next_r = cur_row + dr[i]
            next_c = cur_col + dc[i]
            if 0 <= next_r < row and 0 <= next_c < col and visited[next_r][next_c] == 0 and graph[next_r][next_c] == 'L':
                visited[next_r][next_c] = 1
                q.append((next_r, next_c, dist + 1))


for cur_r in range(row):
    for cur_c in range(col):
        if graph[cur_r][cur_c] == 'L':
            visited = [[0] * col for _ in range(row)]
            bfs(cur_r, cur_c)
            visited.clear()

print(maximum)
