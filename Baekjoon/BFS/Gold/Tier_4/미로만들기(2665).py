from collections import deque
import sys

row = col = int(input())
graph = []
visited = []
flag = True
cnt = 0
for _ in range(row):
    graph.append(list(map(int, sys.stdin.readline().strip())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c, change_cnt):
    q = deque()
    q.append((r, c, change_cnt))
    visited[r][c] = change_cnt

    while q:
        cur_r, cur_c, cur_change_cnt = q.popleft()

        if (cur_r == row - 1) and (cur_c == col - 1):
            print(cnt)
            exit(0)

        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]

            if 0 <= next_r < row and 0 <= next_c < col:

                if graph[next_r][next_c] == 1 and visited[next_r][next_c] < cur_change_cnt:
                    visited[next_r][next_c] = cur_change_cnt
                    q.append((next_r, next_c, cur_change_cnt))
                elif graph[next_r][next_c] == 0 and cur_change_cnt > 0 and visited[next_r][next_c] < cur_change_cnt - 1:
                    visited[next_r][next_c] = cur_change_cnt - 1
                    q.append((next_r, next_c, cur_change_cnt - 1))


while flag:
    for _ in range(row):
        visited.append([-1] * col)

    bfs(0, 0, cnt)

    cnt += 1
    visited.clear()
