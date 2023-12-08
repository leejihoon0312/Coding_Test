from collections import deque
import sys

row, col = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(row)]
visited = [[0] * col for _ in range(row)]
q = deque()
cnt = 0

for cur_row in range(row):
    for cur_col in range(col):
        if graph[cur_row][cur_col] == 'I':
            q.append((cur_row, cur_col))
            visited[cur_row][cur_col] = 1
            break

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(q):
    global cnt

    while q:
        cur_r, cur_c = q.popleft()
        if graph[cur_r][cur_c] == 'P':
            cnt += 1
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < row and 0 <= next_c < col and visited[next_r][next_c] == 0 and graph[next_r][next_c] != 'X':
                q.append((next_r, next_c))
                visited[next_r][next_c] = 1


bfs(q)

if cnt > 0:
    print(cnt)
else:
    print('TT')
