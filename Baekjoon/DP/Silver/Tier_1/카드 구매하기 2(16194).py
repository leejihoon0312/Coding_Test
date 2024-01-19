import sys

N = int(input())

cost = [0] + list(map(int, sys.stdin.readline().split()))

dp = [10 ** 10 for _ in range(N + 1)]

dp[1] = cost[1]


def DP():
    for quantity in range(2, N + 1):
        for step in range(1, int(quantity / 2) + 1):
            dp[quantity] = min(cost[1] * quantity, cost[quantity], dp[step] + dp[quantity - step], dp[quantity])

    return dp[N]


print(DP())
