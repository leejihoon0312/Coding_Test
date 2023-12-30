import sys
def backtracking(arr):

    if len(arr) == 6:
        print(" ".join(arr))
        return

    for num in num_ls:
        if num not in arr:
            if len(arr) == 0:
                arr.append(num)
                backtracking(arr[:])
                arr.pop()
            elif len(arr) != 0 and int(arr[-1]) < int(num):
                arr.append(num)
                backtracking(arr[:])
                arr.pop()

cnt = 0
while True:
    ls = list(sys.stdin.readline().split())

    if ls[0] == "0":
        break

    num_ls = ls[1:]

    if cnt!=0:
        print()
    backtracking([])
    cnt += 1

