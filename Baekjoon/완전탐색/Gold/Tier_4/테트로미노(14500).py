import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
visited = [[0] * col for _ in range(row)]
maximum = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(cur_r, cur_c, total, depth):
    global maximum
    visited[cur_r][cur_c] = 1

    if total > maximum:
        maximum = total

    if depth == 4:
        return

    for i in range(4):
        next_r = cur_r + dr[i]
        next_c = cur_c + dc[i]
        if 0 <= next_r < row and 0 <= next_c < col and visited[next_r][next_c] == 0:
            dfs(next_r, next_c, total + graph[next_r][next_c], depth + 1)
            visited[next_r][next_c] = 0


def bfs(cur_r, cur_c, depth):
    q = deque()
    q.append((cur_r, cur_c, depth))
    global temp
    while q:
        cur_ro, cur_co, cur_depth = q.popleft()

        if cur_depth == 1:
            continue

        for i in range(4):
            next_ro = cur_ro + dr[i]
            next_co = cur_co + dc[i]
            if 0 <= next_ro < row and 0 <= next_co < col and visited[next_ro][next_co] == 0:
                temp.append(graph[next_ro][next_co])
                q.append((next_ro, next_co, depth + 1))


for r in range(row):
    for c in range(col):
        temp = []

        dfs(r, c, graph[r][c], 1)
        bfs(r, c, 0)
        if len(temp) == 3 and maximum <= sum(temp) + graph[r][c]:
            maximum = sum(temp) + graph[r][c]
        if len(temp) == 4:
            for i in temp:
                if maximum <= sum(temp) - i + graph[r][c]:
                    maximum = sum(temp) - i + graph[r][c]

        visited[r][c] = 0

print(maximum)
