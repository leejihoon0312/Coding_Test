from collections import deque
import sys

row, col = map(int, sys.stdin.readline().split())
graph = []
visited = []
result = []
answer = 0
for _ in range(row):
    graph.append(list(map(int, sys.stdin.readline().split())))
    visited.append([0]*col)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    global cnt
    while q:
        cur_r, cur_c = q.popleft()

        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0<=next_r<row and 0<=next_c<col and visited[next_r][next_c] == 0:
                if graph[next_r][next_c] == 0:
                    visited[next_r][next_c] = 1
                    q.append((next_r, next_c))
                else:
                    cnt += 1
                    visited[next_r][next_c] = 1
                    graph[next_r][next_c] = 0


flag = True
while flag:
    for _ in range(row):
        visited.append([0] * col)
    flag = False
    cnt = 0
    bfs(0,0)
    if cnt > 0:
        flag = True
        answer = cnt
        result.append(cnt)
    visited.clear()

print(len(result))
print(answer)
