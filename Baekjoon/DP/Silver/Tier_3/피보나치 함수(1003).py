T = int(input())

memo = {0: [1, 0], 1: [0, 1]}


def DP(number):
    if number not in memo:
        case1 = DP(number - 1)
        case2 = DP(number - 2)

        memo[number] = [case1[0] + case2[0], case1[1] + case2[1]]

    return memo[number]


for _ in range(T):
    num = int(input())

    result = DP(num)

    print(f"{result[0]} {result[1]}")
