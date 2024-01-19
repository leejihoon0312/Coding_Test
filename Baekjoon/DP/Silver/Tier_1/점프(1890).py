import sys

N = int(input())

graph = [[0] * (N + 1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * (N + 1) for _ in range(N + 1)]

dp[1][1] = 1


def DP(cur_r, cur_c):
    init = 0

    for row in range(1, 10):
        if cur_r - row >= 1 and graph[cur_r - row][cur_c] == row:
            init += dp[cur_r - row][cur_c]

    for col in range(1, 10):
        if cur_c - col >= 1 and graph[cur_r][cur_c - col] == col:
            init += dp[cur_r][cur_c - col]

    dp[cur_r][cur_c] = init


for r in range(1, N+1):
    for c in range(1, N+1):
        if r==c==1:
            continue
        DP(r, c)

print(dp[N][N])
