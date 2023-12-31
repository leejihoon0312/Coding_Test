import sys
from collections import Counter

A, B = sys.stdin.readline().split()
if len(A) > len(B):
    print(-1)
    exit(0)
num_dict = Counter(A)
max_num = 0


def backtracking(arr):
    global max_num

    if len(arr) == len(A):
        if int("".join(arr)) < int(B):
            max_num = max(max_num, int("".join(arr)))
            return
        return

    for key in num_dict.keys():
        if num_dict[key] > 0:
            arr.append(key)
            num_dict[key] -= 1
            backtracking(arr[:])
            num_dict[key] += 1
            arr.pop()


for start_num in num_dict.keys():
    if start_num == '0':
        continue
    else:
        num_dict[start_num] -= 1
        backtracking([start_num])
        num_dict[start_num] += 1
if max_num != 0:
    print(max_num)
else:
    print(-1)
