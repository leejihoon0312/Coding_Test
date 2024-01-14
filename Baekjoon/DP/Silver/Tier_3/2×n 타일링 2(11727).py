N = int(input())

memo = {1: 1, 2: 3}


def DP():
    for i in range(3, N + 1):
        memo[i] = memo[i - 1] + memo[i - 2] * 2

    return memo[N]


print(DP()%10007)
