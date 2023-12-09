from itertools import permutations
import sys

num = int(input())
num_arr = list(sys.stdin.readline().split())
symbol = list(map(int, sys.stdin.readline().split()))
symbol_arr = []
arr = ["+", "-", "*", "/"]
maximum = -1000000000
minimum = 1000000000
for i in range(4):

    if symbol[i] == 0:
        continue
    else:
        for j in range(symbol[i]):
            symbol_arr.append(arr[i])
ls = set(permutations(symbol_arr, num - 1))
for sym in ls:
    temp = int(eval(num_arr[0] + sym[0] + num_arr[1]))


    for i in range(1, num - 1):
        temp = int(eval(str(temp) + sym[i] + num_arr[i + 1]))

    maximum = max(maximum, temp)
    minimum = min(minimum, temp)

print(maximum)
print(minimum)
