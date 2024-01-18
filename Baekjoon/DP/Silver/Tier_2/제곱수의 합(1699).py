import math

N = int(input())

memo = {0: 0, 1: 1, 2: 2, 3: 3, 4: 1}


def DP():
    for num in range(5, N + 1):
        if num == int(math.sqrt(num)) ** 2:
            memo[num] = 1
            continue
        init = 10 ** 10
        for step in range(1, int(math.sqrt(num)) + 1):
            if memo[step ** 2] + memo[num - step ** 2] < init:
                init = memo[step ** 2] + memo[num - step ** 2]

        memo[num] = init

    return memo[N]


print(DP())
