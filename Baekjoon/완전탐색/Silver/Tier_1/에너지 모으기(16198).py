import sys

sys.setrecursionlimit(10 ** 6)
number = int(input())

arr = list(map(int, sys.stdin.readline().split()))
result = 0


def dfs(maximum, array):
    global result
    if maximum > result:
        result = maximum

    for i in range(1, len(array) - 1):
        weight = maximum + (array[i - 1] * array[i + 1])
        copy_arr = array.copy()
        del copy_arr[i]
        dfs(weight, copy_arr)


dfs(0, arr.copy())

print(result)
