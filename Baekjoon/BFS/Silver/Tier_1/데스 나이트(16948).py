from collections import deque

row = col = int(input())

start_r, start_c, end_r, end_c = map(int, input().split())

graph = [[0] * col for _ in range(row)]
visited = [[0] * col for _ in range(row)]

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]


def bfs(r, c):
    q = deque()
    q.append((r, c, 0))
    visited[r][c] = 1
    graph[r][c] = 0

    while q:
        cur_r, cur_c, dist = q.popleft()

        if cur_r == end_r and cur_c == end_c:
            print(dist)
            exit(0)

        for i in range(6):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row and 0 <= next_c < col and visited[next_r][next_c] == 0 and graph[next_r][next_c] == 0:
                visited[next_r][next_c] = 1
                graph[next_r][next_c] = dist + 1
                q.append((next_r, next_c, dist + 1))


bfs(start_r, start_c)
print(-1)
