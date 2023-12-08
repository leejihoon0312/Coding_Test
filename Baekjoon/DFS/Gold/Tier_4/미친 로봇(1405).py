
import sys
sys.setrecursionlimit(10**6)
times, E, W, S, N = map(int, input().split())
row = col = times

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

direction = [N * 0.01, S * 0.01, E * 0.01, W * 0.01]

graph = [[0] * (2 * times + 1) for _ in range(2 * times + 1)]
visited = [[0] * (2 * times + 1) for _ in range(2 * times + 1)]
answer = 0


def dfs(r, c, probability, move):
    visited[r][c] = 1
    global answer
    if move == times:
        answer += probability
        return

    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0 <= next_r < (2 * row + 1) and 0 <= next_c < (2 * col + 1) and visited[next_r][next_c] == 0:
            dfs(next_r, next_c, probability * direction[i], move + 1)
            visited[next_r][next_c] = 0


dfs(row, col, 1, 0)

print(answer)
