from collections import deque
import sys

row, col = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(row)]
visited = [[0] * col for _ in range(row)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    q = deque()
    q.append((r, c, 1))
    visited[r][c] = 1

    while q:
        cur_r, cur_c, dist = q.popleft()
        if cur_r == row - 1 and cur_c == col - 1:
            print(dist)
            exit(0)

        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row and 0 <= next_c < col and visited[next_r][next_c] == 0 and graph[next_r][next_c] == 1:
                visited[next_r][next_c] = 1
                q.append((next_r, next_c, dist + 1))


bfs(0, 0)
