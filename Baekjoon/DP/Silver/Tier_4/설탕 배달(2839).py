import sys

sys.setrecursionlimit(10 ** 5)
kg = int(input())
memo = {}


def DP(weight):
    if weight <= 5:
        if weight == 3 or weight == 5:
            return 1
        else:
            return False

    if weight not in memo:
        minus3 = DP(weight - 3)
        minus5 = DP(weight - 5)

        if not minus3 and not minus5:
            memo[weight] = False
        elif minus3 and minus5:
            memo[weight] = min(minus3 + 1, minus5 + 1)
        elif minus3:
            memo[weight] = minus3 + 1
        elif minus5:
            memo[weight] = minus5 + 1

    return memo[weight]


result = DP(kg)

if result:
    print(result)
else:
    print(-1)
