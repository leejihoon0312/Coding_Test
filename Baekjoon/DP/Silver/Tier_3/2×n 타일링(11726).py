N = int(input())

memo = {1: 1, 2: 2}


def DP(number):
    if number not in memo:
        memo[number] = DP(number - 1) + DP(number - 2)

    return memo[number]


print(DP(N)%10007)
