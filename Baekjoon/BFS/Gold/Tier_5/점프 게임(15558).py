from collections import deque
import sys

size, move = map(int, input().split())

graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(2)]
visited = [[0] * size for _ in range(2)]

dr = [0, 0, 0]
dc = [1, -1, move]


def bfs(r, c):
    q = deque()
    q.append((r, c, 0))
    visited[r][c] = 1

    while q:
        cur_r, cur_c, cnt = q.popleft()

        for i in range(3):
            if i == 2 and cur_r == 1:
                dr[2] = -1
            elif i == 2 and cur_r == 0:
                dr[2] = 1

            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]

            if next_c >= size:
                print(1)
                exit(0)

            if 0 <= next_r <= 1 and cnt < next_c < size and visited[next_r][next_c] == 0 and graph[next_r][next_c] == 1:
                visited[next_r][next_c] = 1
                q.append((next_r, next_c, cnt + 1))


bfs(0, 0)
print(0)
