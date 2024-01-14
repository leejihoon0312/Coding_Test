N = int(input())

wine = [0] + [int(input()) for _ in range(N)]

if N == 1:
    print(wine[1])
    exit(0)

memo = {0: 0, 1: wine[1], 2: wine[1] + wine[2]}

max_num = memo[2]


def DP():
    global max_num
    for i in range(3, N + 1):
        memo[i] = max(memo[i - 2] + wine[i], memo[i - 3] + wine[i - 1] + wine[i], max_num)
        max_num = memo[i]
    return memo[N]


print(DP())
