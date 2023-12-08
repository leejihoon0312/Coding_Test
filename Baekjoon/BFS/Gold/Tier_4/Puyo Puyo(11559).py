from collections import deque
import sys

graph = []
visited = []
flag = True
destroy = 0

for _ in range(12):
    graph.append(list(sys.stdin.readline().strip()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, color):
    q = deque()
    q.append((r, c, color))
    visited[r][c] = 1
    temp.append((r, c))
    global cnt
    while q:
        cur_r, cur_c, cur_color = q.popleft()

        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < 12 and 0 <= next_c < 6 and visited[next_r][next_c] == 0 and graph[next_r][next_c] == cur_color:
                cnt += 1
                temp.append((next_r, next_c))
                visited[next_r][next_c] = 1
                q.append((next_r, next_c, cur_color))


while flag:
    flag = False
    isspace = False
    for _ in range(12):
        visited.append([0] * 6)

    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and visited[i][j] == 0:
                cnt = 1
                temp = []
                bfs(i, j, graph[i][j])
                if cnt >= 4:
                    isspace = True
                    flag = True
                    for r, c in temp:
                        graph[r][c] = '.'

    # 빈 공간으로 뿌요 내리기
    if isspace:
        destroy += 1
        for col in range(6):
            dot = deque()
            for row in range(11, -1, -1):
                if graph[row][col] == ".":
                    dot.append((row, col))
                if graph[row][col] != "." and len(dot) > 0:
                    r, c = dot.popleft()
                    dot.append((row, col))
                    graph[row][col], graph[r][c] = graph[r][c], graph[row][col]

            dot.clear()

    visited.clear()

print(destroy)
