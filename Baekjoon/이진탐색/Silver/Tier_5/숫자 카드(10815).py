import sys
N = int(input())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
M = int(input())

def bisect(target, start, end, mid):
    while start<=end:
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1

        mid = (start+end) // 2

    return 0
for check in list(map(int, sys.stdin.readline().split())):
    start = 0
    end = len(arr)-1
    mid = (start + end) // 2

    print(bisect(check, start, end, mid), end=" ")