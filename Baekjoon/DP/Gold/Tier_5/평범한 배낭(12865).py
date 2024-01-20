N, K = map(int, input().split())

# [물건 번호][여유 공간]
dp = [[0] * (K + 1) for _ in range(N + 1)]


def DP():
    for stuff_num in range(1, N + 1):
        weight, value = map(int, input().split())

        for empty_space in range(1, K + 1):
            if empty_space < weight:
                dp[stuff_num][empty_space] = dp[stuff_num - 1][empty_space]
            else:
                dp[stuff_num][empty_space] = max(dp[stuff_num - 1][empty_space - weight] + value,
                                                 dp[stuff_num - 1][empty_space], dp[stuff_num][empty_space])

    return dp[N][K]


print(DP())
