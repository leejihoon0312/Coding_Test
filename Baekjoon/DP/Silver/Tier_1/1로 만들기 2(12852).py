from collections import defaultdict

N = int(input())

memo = defaultdict(list)

# [최소 연산 횟수, 어떤 수로 부터 왔는지]
memo[2] = [1, 1]
memo[3] = [1, 1]

if N == 1:
    print(0)
    print(1)
    exit(0)

def DP():
    for num in range(4, N + 1):

        if num % 6 == 0:
            if min(memo[num - 1], memo[int(num / 2)], memo[int(num / 3)]) == memo[num - 1]:
                memo[num] = [memo[num - 1][0] + 1, num - 1]
            elif min(memo[num - 1], memo[int(num / 2)], memo[int(num / 3)]) == memo[int(num / 2)]:
                memo[num] = [memo[int(num / 2)][0] + 1, int(num / 2)]
            else:
                memo[num] = [memo[int(num / 3)][0] + 1, int(num / 3)]

        elif num % 2 == 0:
            if memo[num - 1] < memo[int(num / 2)]:
                memo[num] = [memo[num - 1][0] + 1, num - 1]
            else:
                memo[num] = [memo[int(num / 2)][0] + 1, int(num / 2)]

        elif num % 3 == 0:
            if memo[num - 1] < memo[int(num / 3)]:
                memo[num] = [memo[num - 1][0] + 1, num - 1]
            else:
                memo[num] = [memo[int(num / 3)][0] + 1, int(num / 3)]

        else:
            memo[num] = [memo[num - 1][0] + 1, num - 1]


DP()

print(memo[N][0])

init = N

while True:

    print(init, end=" ")
    init = memo[init][1]
    if init == 1:
        print(1)
        break
