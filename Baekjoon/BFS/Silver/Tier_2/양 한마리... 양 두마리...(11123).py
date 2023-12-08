from collections import deque
import sys

times = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = []
def bfs(r, c):
    q= deque()
    q.append((r, c))
    visited[r][c] = 1

    while q:
        cur_r, cur_c = q.popleft()

        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0<=next_r<row and 0<=next_c<col and visited[next_r][next_c]==0 and graph[next_r][next_c] =='#':
                q.append((next_r, next_c))
                visited[next_r][next_c] = 1


for _ in range(times):
    row, col = map(int, sys.stdin.readline().split())
    graph = [list(sys.stdin.readline().strip()) for _ in range(row)]
    visited = [[0] * col for _ in range(row)]
    cnt = 0
    for cur_row in range(row):
        for cur_col in range(col):
            if visited[cur_row][cur_col] ==0 and graph[cur_row][cur_col] =='#':
                bfs(cur_row, cur_col)
                cnt += 1

    result.append(cnt)
    graph.clear()
    visited.clear()

for i in result:
    print(i)