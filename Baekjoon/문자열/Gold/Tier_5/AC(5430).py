import sys
from collections import Counter

case = int(input())

for _ in range(case):
    function_word = sys.stdin.readline().strip()
    N = int(input())
    arr = sys.stdin.readline().strip()
    cnt_dic = Counter(function_word)
    if cnt_dic["D"] > N:
        print("error")
        continue

    size = len(arr)
    if size> 2:
        num_ls = list(map(int, arr[1:size - 1].split(",")))
    else:
        print("[]")
        continue

    reverse_flag = False
    left_idx = 0
    right_idx = len(num_ls)-1
    for function in function_word:
        if function == "R" :
            if reverse_flag:
                reverse_flag = False
            else:
                reverse_flag = True
        elif function == "D":
            if reverse_flag:
                right_idx -= 1
            else:
                left_idx += 1

    if cnt_dic["R"] % 2 == 0:
        print(str(num_ls[left_idx:right_idx+1]).replace(" ", ""))
    else:
        print(str(num_ls[left_idx:right_idx+1][::-1]).replace(" ", ""))