import sys

row, col, K = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(row)]
visited = [[0]*col for _ in range(row) ]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 0


def backtracking(cur_r, cur_c, cur_dist):
    global K, result

    if cur_dist > K:
        return

    if cur_dist == K and cur_r == 0 and cur_c == col - 1:
        result += 1
        return

    for i in range(4):
        next_r = cur_r + dr[i]
        next_c = cur_c + dc[i]

        if 0 <= next_r < row and 0 <= next_c < col and graph[next_r][next_c] == "." and visited[next_r][next_c] == 0:
            visited[next_r][next_c] = 1
            backtracking(next_r, next_c, cur_dist + 1)
            visited[next_r][next_c] = 0

visited[row - 1][0] = 1
backtracking(row - 1, 0, 1)
print(result)
