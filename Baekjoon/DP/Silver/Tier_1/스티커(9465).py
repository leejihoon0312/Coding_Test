import sys

T = int(input())


def DP(num):
    for i in range(2, N + 1):
        cost[1][i] = max(cost[2][i - 1], cost[1][i - 2], cost[2][i - 2]) + cost[1][i]
        cost[2][i] = max(cost[1][i - 1], cost[1][i - 2], cost[2][i - 2]) + cost[2][i]

    return max(cost[1][num], cost[2][num])


for _ in range(T):
    N = int(input())
    cost = [[0] * (N + 1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(2)]

    print(DP(N))
