def solution(n):
    if n % 2 != 0:
        return 0

    memo = {0: 0, 2: 3, 4: 11}

    for i in range(6, n + 1, 2):
        memo[i] = memo[i - 2] * 3 + (memo[i - 2] - memo[i - 4])

    return memo[n] % 1000000007