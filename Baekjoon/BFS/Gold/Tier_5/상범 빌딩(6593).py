from collections import deque
import sys

dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]


def bfs(h, r, c):
    q = deque()
    q.append((h, r, c, 0))
    visited[h][r][c] = 1
    global flag

    while q:
        cur_h, cur_r, cur_c, cur_dist = q.popleft()

        if graph[cur_h][cur_r][cur_c] == 'E':
            print(f"Escaped in {cur_dist} minute(s).")
            flag = False

        for i in range(6):
            next_h = cur_h + dh[i]
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_h < height and 0 <= next_r < row and 0 <= next_c < col and visited[next_h][next_r][next_c] == 0 and graph[next_h][next_r][next_c] != '#':
                visited[next_h][next_r][next_c] = 1
                q.append((next_h, next_r, next_c, cur_dist + 1))


while True:
    height, row, col = map(int, sys.stdin.readline().split())
    graph = []
    visited = []
    start_h = 0
    start_r = 0
    start_c = 0
    flag = True

    if height == row == col == 0:
        break

    for i in range(height):
        temp_graph = []
        temp_visited = []
        for j in range(row):
            ls = list(sys.stdin.readline().strip())
            if 'S' in ls:
                start_h = i
                start_r = j
                start_c = ls.index('S')

            temp_graph.append(ls)
            temp_visited.append([0] * col)
        graph.append(temp_graph)
        visited.append(temp_visited)
        input()

    bfs(start_h, start_r, start_c)

    if flag:
        print("Trapped!")
