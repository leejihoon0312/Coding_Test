from itertools import combinations
from collections import deque
import sys

row, max_shop = map(int, sys.stdin.readline().split())
col = row
graph = []
home = []
shop = []
minimum = 10 ** 9
for i in range(row):
    ls = list(map(int, sys.stdin.readline().split()))
    for j in range(col):
        if ls[j] == 1:
            home.append((i, j))
        if ls[j] == 2:
            shop.append((i, j))

    graph.append(ls)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(queue):
    global total_dist, count, minimum
    while queue:
        cur_r, cur_c, cur_dist = queue.popleft()

        if count == len(home) and minimum > total_dist:
            minimum = total_dist
        if count < len(home) and minimum < total_dist:
            break

        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row and 0 <= next_c < col and visited[next_r][next_c] == 0:

                if graph[next_r][next_c] == 1:
                    total_dist += cur_dist + 1
                    count += 1
                    visited[next_r][next_c] = 1
                    q.append((next_r, next_c, cur_dist + 1))

                if graph[next_r][next_c] != 1:
                    visited[next_r][next_c] = 1
                    q.append((next_r, next_c, cur_dist + 1))


for left in range(1, max_shop + 1):
    c = combinations(shop, left)

    for ls in c:
        q = deque()
        visited = [[0] * col for _ in range(row)]
        total_dist = 0
        count = 0
        for r, c in ls:
            q.append((r, c, 0))
            visited[r][c] = 1
        bfs(q)
        visited.clear()

print(minimum)
