N, M = map(int, input().split())

cost = [int(input()) for _ in range(N)]

start = max(cost)
end = sum(cost)


def bisect(start, end):
    min_cost = 10 ** 10

    while start <= end:
        mid = (start + end) // 2

        days = 1
        left_cost = mid
        for money in cost:
            if left_cost - money >= 0:
                left_cost -= money
            else:
                left_cost = mid
                days += 1
                left_cost -= money

        if days <= M:
            min_cost = min(min_cost, mid)
            end = mid - 1
        elif days > M:
            start = mid + 1

    return min_cost


print(bisect(start, end))
