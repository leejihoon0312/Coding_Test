import sys

K, N = map(int, input().split())

lans = [int(input()) for _ in range(K)]

start = 1
end = max(lans)
mid = min(lans)


def bisect(start, end):
    max_len = 0
    while start <= end:
        mid = (start + end) // 2

        total_lan = 0
        for lan in lans:
            total_lan += lan // mid

        if total_lan >= N:
            max_len = max(max_len, mid)
            start = mid + 1
        elif total_lan < N:
            end = mid - 1

    return max_len


print(bisect(start, end))
