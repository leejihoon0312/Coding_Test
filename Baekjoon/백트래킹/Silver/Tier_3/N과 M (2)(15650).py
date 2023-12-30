N, M = map(int, input().split())


def backtracking(std_num, array):
    if len(array) == M:
        for i in array:
            print(i, end=" ")
        print()

    for number in range(std_num + 1, N + 1):
        if number not in array:
            array.append(number)
            backtracking(number, array[:])
            array.pop()


for num in range(1, N + 1):
    arr = [num]
    backtracking(num, arr)
