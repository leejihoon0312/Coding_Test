import sys

N, M = map(int, input().split())

lectures = list(map(int, sys.stdin.readline().split()))

start = max(lectures)
end = sum(lectures)


def bisect(start, end):
    min_length = sum(lectures)

    while start <= end:

        mid = (start + end) // 2

        tapes = 1
        temp = mid
        for lecture in lectures:
            if temp - lecture >= 0:
                temp -= lecture
            else:
                temp = mid
                tapes += 1
                temp -= lecture

        if tapes <= M:
            min_length = min(min_length, mid)
            end = mid - 1
        elif tapes > M:
            start = mid + 1

    return min_length


print(bisect(start, end))
