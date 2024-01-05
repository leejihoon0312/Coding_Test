N = int(input())


def check(array):
    for size in range(2, int(len(array) / 2) + 1):
        for start in range(len(array) - (size * 2) + 1):
            if ("".join(array[start:size+start])) == ("".join(array[start + size:size * 2+start])):
                return False

    return True


def backtracking(arr):

    if len(arr) >= 4:
        if not check(arr):
            return

    if len(arr) == N:
        print("".join(arr))
        exit(0)


    for num in range(1, 4):
        if arr[-1] != str(num):
            arr.append(str(num))
            backtracking(arr[:])
            arr.pop()


for i in range(1, 4):
    backtracking([str(i)])
