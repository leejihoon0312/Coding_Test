import sys

N = int(sys.stdin.readline())

result = 0

vertical = dict()


def check(cur_row, col, ls):
    for chk_r, chk_c in ls:
        if abs(cur_row - chk_r) == abs(col - chk_c):
            return False
    return True


def backtracking(cur_row, position):
    global result

    if cur_row == N:
        result += 1
        return

    for col in range(N):

        if col in vertical:
            continue

        if check(cur_row, col, position):
            position.append((cur_row, col))
            vertical[col] = 1
            backtracking(cur_row + 1, position)
            position.pop()
            del vertical[col]


backtracking(0, [])
print(result)
