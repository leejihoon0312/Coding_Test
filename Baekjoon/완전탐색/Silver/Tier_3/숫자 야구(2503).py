from itertools import permutations
times = int(input())

num_list = list( permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 3) )
for _ in range(times):
    number, strike, ball = map(int, input().split(" "))
    string_num = str(number)
    cnt = 0

    for i in range(len(num_list)):
        s = b = 0
        i -= cnt
        for j in range(3):
            if num_list[i][j] == string_num[j]:
                s += 1
            elif string_num[j] in num_list[i]:
                b += 1

        if (strike != s) or (ball != b):
            num_list.remove(num_list[i])
            cnt += 1

print(len(num_list))



