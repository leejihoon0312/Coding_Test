from collections import deque
import sys

row, col = map(int, input().split())

graph = []

start = []
for i in range(row):
    ls = list(sys.stdin.readline().strip())
    for j in range(len(ls)):
        if ls[j] == 'o':
            start.append(i)
            start.append(j)
    graph.append(ls)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r1, c1, r2, c2):
    q = deque()
    q.append((r1, c1, r2, c2, count))

    while q:
        cur_r1, cur_c1, cur_r2, cur_c2, cur_count = q.popleft()

        for i in range(4):
            out = 0
            next_r1 = cur_r1 + dr[i]
            next_c1 = cur_c1 + dc[i]
            next_r2 = cur_r2 + dr[i]
            next_c2 = cur_c2 + dc[i]

            if (next_r1 < 0 or next_r1 >= row) or (next_c1 < 0 or next_c1 >= col):
                out += 1

            if (next_r2 < 0 or next_r2 >= row) or (next_c2 < 0 or next_c2 >= col):
                out += 1

            if out == 2:
                continue
            if out == 1:
                print(count + 1)
                exit(0)

            if graph[next_r1][next_c1] != "#" and graph[next_r2][next_c2] != "#" and cur_count > 0:
                q.append((next_r1, next_c1, next_r2, next_c2, cur_count - 1))

            if graph[next_r1][next_c1] == "#" and graph[next_r2][next_c2] != "#" and cur_count > 0:
                q.append((cur_r1, cur_c1, next_r2, next_c2, cur_count - 1))

            if graph[next_r1][next_c1] != "#" and graph[next_r2][next_c2] == "#" and cur_count > 0:
                q.append((next_r1, next_c1, cur_r2, cur_c2, cur_count - 1))

            if graph[next_r1][next_c1] == "#" and graph[next_r2][next_c2] == "#" and cur_count > 0:
                q.append((cur_r1, cur_c1, cur_r2, cur_c2, cur_count - 1))


for count in range(10):
    row1, col1, row2, col2 = start[0], start[1], start[2], start[3]
    bfs(row1, col1, row2, col2)

print(-1)
