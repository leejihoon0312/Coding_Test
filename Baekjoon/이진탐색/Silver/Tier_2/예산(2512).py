import sys

N = int(input())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
max_budget = int(input())

start = 1
end = max(arr)
mid = min(arr)


def bisect(start, end, mid):
    while start <= end:

        budget = 0
        for cost in arr:
            if cost <= mid:
                budget = budget + cost
            else:
                budget = budget + mid

        if budget == max_budget:
            return mid
        elif budget < max_budget:
            start = mid + 1
        else:
            end = mid - 1

        mid = (start + end) // 2

    return end


if sum(arr) <= max_budget:
    print(max(arr))
    exit(0)
else:
    print(bisect(start, end, mid))
