import sys

row = col = int(input())

graph = []
maximum = 0

for _ in range(row):
    graph.append(list(sys.stdin.readline().strip()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(start_r, start_c, updown, find_color):
    visited[start_r][start_c] = 1
    global tb, lr
    if updown:
        for i in range(0, 2):
            next_r = start_r + dr[i]
            next_c = start_c + dc[i]
            if 0 <= next_r < row and 0 <= next_c < col and visited[next_r][next_c] == 0 and graph[next_r][next_c] == find_color:
                tb += 1
                dfs(next_r, next_c, updown, find_color)

    if not updown:
        for i in range(2, 4):
            next_r = start_r + dr[i]
            next_c = start_c + dc[i]
            if 0 <= next_r < row and 0 <= next_c < col and visited[next_r][next_c] == 0 and graph[next_r][next_c] == find_color:
                lr += 1
                dfs(next_r, next_c, updown, find_color)


for r in range(row):
    for c in range(col):

        if c + 1 < col and graph[r][c] != graph[r][c + 1]:
            tb = 1
            lr = 1
            visited = [[0] * col for _ in range(row)]
            graph[r][c], graph[r][c + 1] = graph[r][c + 1], graph[r][c]
            dfs(r, c, True, graph[r][c])
            dfs(r, c, False, graph[r][c])
            visited.clear()
            maximum = max(maximum, tb, lr)

            tb = 1
            lr = 1
            visited = [[0] * col for _ in range(row)]
            dfs(r, c + 1, True, graph[r][c + 1])
            dfs(r, c + 1, False, graph[r][c + 1])
            visited.clear()
            graph[r][c], graph[r][c + 1] = graph[r][c + 1], graph[r][c]
            maximum = max(maximum, tb, lr)

        if c + 1 < col and graph[r][c] == graph[r][c + 1]:
            tb = 1
            lr = 1
            visited = [[0] * col for _ in range(row)]
            dfs(r, c, True, graph[r][c])
            dfs(r, c, False, graph[r][c])
            visited.clear()
            maximum = max(maximum, tb, lr)

            tb = 1
            lr = 1
            visited = [[0] * col for _ in range(row)]
            dfs(r, c + 1, True, graph[r][c + 1])
            dfs(r, c + 1, False, graph[r][c + 1])
            visited.clear()
            maximum = max(maximum, tb, lr)

        if r + 1 < row and graph[r][c] != graph[r + 1][c]:
            tb = 1
            lr = 1
            visited = [[0] * col for _ in range(row)]
            graph[r][c], graph[r + 1][c] = graph[r + 1][c], graph[r][c]
            dfs(r, c, True, graph[r][c])
            dfs(r, c, False, graph[r][c])
            visited.clear()
            maximum = max(maximum, tb, lr)

            tb = 1
            lr = 1
            visited = [[0] * col for _ in range(row)]
            dfs(r + 1, c, True, graph[r + 1][c])
            dfs(r + 1, c, False, graph[r + 1][c])
            graph[r][c], graph[r + 1][c] = graph[r + 1][c], graph[r][c]
            visited.clear()
            maximum = max(maximum, tb, lr)

        if r + 1 < row and graph[r][c] == graph[r + 1][c]:
            tb = 1
            lr = 1
            visited = [[0] * col for _ in range(row)]
            dfs(r, c, True, graph[r][c])
            dfs(r, c, False, graph[r][c])
            visited.clear()
            maximum = max(maximum, tb, lr)

            tb = 1
            lr = 1
            visited = [[0] * col for _ in range(row)]
            dfs(r + 1, c, True, graph[r + 1][c])
            dfs(r + 1, c, False, graph[r + 1][c])
            visited.clear()
            maximum = max(maximum, tb, lr)

print(maximum)
