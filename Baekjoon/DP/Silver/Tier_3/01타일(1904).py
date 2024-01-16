N = int(input())

if N==1:
    print(1)
    exit(0)

memo = [[0] for _ in range(N + 1)]

memo[1] = 1
memo[2] = 2


def DP():
    for i in range(3, N + 1):
        memo[i] = (memo[i - 1] + memo[i - 2]) % 15746

        # memo[i][0] = (memo[i - 2][1] + memo[i - 2][0]) % 15746
        # memo[i][1] = (memo[i - 1][1] + memo[i - 1][0]) % 15746

    return memo[N] % 15746


print(DP())
