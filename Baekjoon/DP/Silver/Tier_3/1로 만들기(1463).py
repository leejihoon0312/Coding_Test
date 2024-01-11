# N = int(input())
#
# memo = {1: 0}
#
#
# def DP(number):
#     for num in range(1, N + 1):
#
#         if num + 1 not in memo or memo[num + 1] > memo[num] + 1:
#             memo[num + 1] = memo[num] + 1
#         if num * 2 not in memo or memo[num * 2] > memo[num] + 1:
#             memo[num * 2] = memo[num] + 1
#         if num * 3 not in memo or memo[num * 3] > memo[num] + 1:
#             memo[num * 3] = memo[num] + 1
#
#     return memo[number]
#
#
# print(DP(N))

N = int(input())

memo = {}


def DP(number):
    if number == 1:
        return 0

    if number not in memo:

        case1 = 10 ** 6 + 1
        case2 = 10 ** 6 + 1
        case3 = 10 ** 6 + 1
        case4 = 10 ** 6 + 1

        if number % 6 == 0:
            case4 = min(DP(int(number / 3)) + 1, DP(int(number / 2)) + 1)

        elif number % 3 == 0:
            case1 = min(DP(int(number / 3)) + 1, DP(number - 1) + 1)

        elif number % 2 == 0:
            case2 = min(DP(int(number / 2)) + 1, DP(number - 1) + 1)
        else:
            case3 = DP(number - 1) + 1

        memo[number] = min(case1, case2, case3, case4)

    return memo[number]


print(DP(N))