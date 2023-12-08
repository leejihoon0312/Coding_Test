times = int(input())
check = []
formula = []
for _ in range(times):
    check.append(int(input()))


def solution(num):
    for init in range(1, num):
        calc = init * (init + 1) / 2
        if calc >= num:
            break
        else:
            formula.append(calc)

    for first in formula:
        for second in formula:
            for third in formula:
                if first + second + third == num:
                    formula.clear()
                    return 1

    formula.clear()
    return 0



for num in check:
    print(solution(num))
