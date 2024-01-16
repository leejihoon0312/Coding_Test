import sys

N = int(input())

cost = [0] + list(map(int, sys.stdin.readline().split()))

memo = [[0] for _ in range(N+1)]
memo[1] = cost[1]


def DP():
    for i in range(2, N + 1):
        num = 0
        for j in range(1, int(i / 2)+1):
            num = max(memo[j] + memo[i - j], num)

        memo[i] = max(memo[1] * i, cost[i], num)

    return memo[N]


print(DP())
