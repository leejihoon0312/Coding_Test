import sys

def bisect(target, start, end, mid):
    while start<=end:
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1

        mid = int((end + start) / 2)

    return 0


N = int(input())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
M = int(input())

for number in list(map(int, sys.stdin.readline().split())):
    start = 0
    end = N-1
    mid = int((end+start)/2)
    print(bisect(number, start, end, mid))
