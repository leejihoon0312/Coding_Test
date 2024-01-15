N = int(input())

memo = [[0] * 2 for _ in range(N + 1)]

memo[1][1] = 1


def DP():
    for i in range(2, N + 1):
        for j in range(2):

            if j == 0:
                memo[i][j] = memo[i - 1][1] + memo[i - 1][0]
            elif j == 1:
                memo[i][j] = memo[i - 1][0]

    return sum(memo[N])


print(DP())
