import sys

N = int(input())

formula = sys.stdin.readline().strip()
maximum = -2 ** 31


def calculate(n1, n2, operator):
    if operator == "+":
        return n1 + n2
    if operator == "-":
        return n1 - n2
    if operator == "*":
        return n1 * n2


def dfs(idx, value):
    global maximum
    if idx == N - 1:
        maximum = max(maximum, value)
        return

    # 괄호 추가 없음
    if idx + 2 < N:
        dfs(idx + 2, calculate(value, int(formula[idx + 2]), formula[idx + 1]))

    # 다음 연산자에서 괄호 추가
    if idx + 4 < N:
        dfs(idx + 4, calculate(value, calculate(int(formula[idx + 2]), int(formula[idx + 4]), formula[idx + 3]), formula[idx + 1]))


dfs(0, int(formula[0]))
print(maximum)
