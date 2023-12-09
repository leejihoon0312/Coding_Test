from itertools import permutations
import sys

k = int(input())
arr = list(sys.stdin.readline().split())
maximum = '-1'
minimum = str(10**(k+1))
ls = permutations(range(10), k+1)

for num in ls:
    flag = True
    for i in range(len(arr)):
        if arr[i] == ">" and num[i]<num[i+1]:
            flag = False
            break
        if arr[i] == "<" and num[i]>num[i+1]:
            flag = False
            break

    if flag:
        str_num = ""
        for i in range(len(num)):
            str_num += str(num[i])

        maximum = str_num if int(maximum) < int(str_num) else maximum
        minimum = str_num if int(minimum) > int(str_num) else minimum



print(maximum)
print(minimum)

