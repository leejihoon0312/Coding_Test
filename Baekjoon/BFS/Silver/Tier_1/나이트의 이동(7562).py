from collections import deque
import sys

times = int(input())
result = []

dr = [-2, -2, 2, 2, -1, 1, -1, 1]
dc = [-1, 1, -1, 1, -2, -2, 2, 2]


def bfs(r, c):
    q = deque()
    q.append((r, c, 0))
    graph[r][c] = 1

    while q:
        cur_r, cur_c, move = q.popleft()

        if cur_r == end_r and cur_c == end_c:
            return move

        for i in range(8):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row and 0 <= next_c < col and graph[next_r][next_c] == 0:
                graph[next_r][next_c] = 1
                q.append((next_r, next_c, move + 1))


for _ in range(times):
    row = col = int(input())
    start_r, start_c = map(int, input().split())
    end_r, end_c = map(int, input().split())

    graph = [[0] * col for _ in range(row)]

    result.append(bfs(start_r, start_c))

    graph.clear()

for i in result:
    print(i)
