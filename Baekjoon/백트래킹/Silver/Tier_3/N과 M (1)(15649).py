N, M = map(int, input().split())
result = []


def backtracking(array):
    if len(array) == M:
        result.append(array)
        return

    for loop in range(1, N + 1):
        if str(loop) not in array:
            array.append(str(loop))
            backtracking(array[:])
            array.pop()


for num in range(1, N + 1):
    arr = [str(num)]
    backtracking(arr)

for ls in result:
    print(" ".join(ls))
