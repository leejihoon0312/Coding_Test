stair_num = int(input())

cost = [0] + [int(input()) for _ in range(stair_num)]

if stair_num == 1:
    print(cost[1])
    exit(0)

memo = {0: 0, 1: cost[1], 2: cost[1]+cost[2]}


def DP():
    for i in range(3, stair_num+1):
        memo[i] = max(memo[i-2], memo[i-3] + cost[i-1]) + cost[i]

    return memo[stair_num]


print(DP())
