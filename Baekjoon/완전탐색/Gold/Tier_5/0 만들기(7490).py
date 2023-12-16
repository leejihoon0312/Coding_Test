from itertools import product

case = int(input())
arr = []
symbol = [" ", "+", "-"]
for _ in range(case):
    num = int(input())
    arr.append(num)

for i in arr:
    per = list(product(symbol, repeat=i - 1))
    temp = []

    for sym in per:
        formula = ""
        for start in range(i - 1):
            formula += str(start + 1) + sym[start]
        formula += str(i)
        if int(eval(formula.replace(" ", ""))) == 0:
            temp.append(formula)

    for j in temp:
        print(j)

    if arr[len(arr) - 1] == i:
        exit(0)
    print()
