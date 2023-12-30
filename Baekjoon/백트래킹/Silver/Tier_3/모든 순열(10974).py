N = int(input())


def backtracking(arr):
    if len(arr) == N:
        print(" ".join(list(map(str, arr))))

    for num in range(1, N + 1):
        if num not in arr:
            arr.append(num)
            backtracking(arr[:])
            arr.pop()


for start in range(1, N + 1):
    backtracking([start])
