import sys

N = int(input())

number_ls = list(map(int, sys.stdin.readline().split()))

symbol = list(map(int, sys.stdin.readline().split()))

max_depth = len(number_ls) - 1

max_num = -(10**10+1)

min_num = 10**10+1
def backtracking(cur_depth, plus, minus, mul, div, calc_result):

    global max_num, min_num

    if cur_depth == max_depth:
        max_num = max(max_num, calc_result)
        min_num = min(min_num, calc_result)
        return

    if plus:
        calc_result += number_ls[cur_depth+1]
        backtracking(cur_depth+1, plus-1, minus, mul, div, calc_result)
        calc_result -= number_ls[cur_depth + 1]

    if minus:
        calc_result -= number_ls[cur_depth+1]
        backtracking(cur_depth+1, plus, minus-1, mul, div, calc_result)
        calc_result += number_ls[cur_depth + 1]

    if mul:
        calc_result *= number_ls[cur_depth+1]
        backtracking(cur_depth+1, plus, minus, mul-1, div, calc_result)
        calc_result = int(calc_result/number_ls[cur_depth + 1])

    if div:
        temp = calc_result
        calc_result = int(calc_result/number_ls[cur_depth + 1])
        backtracking(cur_depth+1, plus, minus, mul, div-1, calc_result)
        calc_result = temp


backtracking(0, symbol[0], symbol[1],symbol[2],symbol[3], number_ls[0])

print(max_num)
print(min_num)