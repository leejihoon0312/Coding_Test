import sys

N = int(input())

arr = list(map(int, sys.stdin.readline().split()))
result = [10 ** 10, 10 ** 10]


def bisect(start, end, target):
    temp = [10 ** 10, 10 ** 10]
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] + target == 0:
            print(f"{target} {arr[mid]}")
            exit(0)
        elif arr[mid] + target > 0:
            if abs(sum(temp)) > abs(arr[mid] + target):
                temp.clear()
                temp.append(target)
                temp.append(arr[mid])

            end = mid - 1

        else:
            if abs(sum(temp)) > abs(arr[mid] + target):
                temp.clear()
                temp.append(target)
                temp.append(arr[mid])
            start = mid + 1
    return temp


for number in range(N - 1):
    start = number + 1
    end = N - 1
    target = arr[number]
    ls = bisect(start, end, target)
    if abs(sum(result)) > abs(sum(ls)):
        result.clear()
        result.append(ls[0])
        result.append(ls[1])

print(f"{result[0]} {result[1]}")
