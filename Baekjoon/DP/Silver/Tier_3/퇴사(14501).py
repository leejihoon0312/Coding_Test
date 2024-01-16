
N = int(input())

memo = [0 for _ in range(N+1)]

def DP():

    for i in range(1, N+1):
        time, cost = map(int, input().split())

        if i + time -1 <= N:
            memo[i + time -1] = max(memo[i + time -1], cost+max(memo[:i]))

    return max(memo)

print(DP())