import sys

sys.setrecursionlimit(10 ** 6)

n, minimum, maximum = map(int, input().split())
row = col = n

graph = [list(map(int, sys.stdin.readline().split())) for I in range(row)]
visited = [[0] * col for _ in range(row)]
change = []
day = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    visited[r][c] = 1
    global sum, cnt
    change.append((r, c))
    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0 <= next_r < row and 0 <= next_c < col and visited[next_r][next_c] == 0 and minimum <= abs(graph[r][c] - graph[next_r][next_c]) <= maximum:
            cnt += 1
            sum += graph[next_r][next_c]
            dfs(next_r, next_c)


while True:
    visited = [[0] * col for _ in range(row)]
    flag = False
    for cur_row in range(row):
        for cur_col in range(col):
            if visited[cur_row][cur_col] == 0:
                sum = graph[cur_row][cur_col]
                cnt = 1
                dfs(cur_row, cur_col)
                if cnt > 1:
                    change_num = int(sum / cnt)
                    for r, c in change:
                        graph[r][c] = change_num
                    flag = True
                    change.clear()
                else:
                    change.clear()

    if not flag:
        print(day)
        exit(0)

    day += 1