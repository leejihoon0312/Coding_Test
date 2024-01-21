X, Y = map(int, input().split())

Z = (Y * 100) // X
if Z >= 99:
    print(-1)
    exit(0)

start = 1
end = 10 ** 9


def bisect(start, end):
    while start <= end:
        mid = (start + end) // 2

        if (Y + mid)* 100 // (X + mid)  == Z:
            start = mid + 1
        elif (Y + mid)* 100 // (X + mid) > Z:
            end = mid - 1

    return start


print(bisect(start, end))
