
N = int(input())

dp = [[0 ] *(10)] + [[0 ] *(10) for _ in range(N)]

for i in range(10):
    dp[1][i] = 1
def DP():

    for length in range(2, N+ 1):
        for last_num in range(10):
            init = 0
            for step in range(last_num + 1):
                init += dp[length - 1][step]

            dp[length][last_num] = init % 10007

    return sum(dp[N]) % 10007


print(DP())
