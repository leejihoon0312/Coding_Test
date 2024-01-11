T = int(input())

memo = {1: 1, 2: 2, 3: 4}


def DP(number):
    if number not in memo:
        memo[number] = DP(number - 1) + DP(number - 2) + DP(number - 3)

    return memo[number]


for _ in range(T):
    num = int(input())
    print(DP(num))
