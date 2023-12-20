from itertools import combinations
from collections import deque
import sys

graph = [list(sys.stdin.readline().strip()) for _ in range(5)]
arr = [[i, j] for i in range(5) for j in range(5)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 0


def bfs(row, col):
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    global depth
    while q:
        cur_r, cur_c = q.popleft()
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < 5 and 0 <= next_c < 5 and visited[next_r][next_c] == 0:
                if [next_r, next_c] in ls:
                    visited[next_r][next_c] = 1
                    depth += 1
                    q.append((next_r, next_c))


for com in list(combinations(arr, 7)):
    ls = list(com)
    doyeon = 0
    dasom = 0
    depth = 1
    visited = [[0] * 5 for _ in range(5)]
    for r, c in ls:
        if graph[r][c] == "Y":
            doyeon += 1
        else:
            dasom += 1
    if dasom < 4:
        continue

    bfs(ls[0][0], ls[0][1])

    if depth == 7:
        result += 1
    visited.clear()
print(result)
