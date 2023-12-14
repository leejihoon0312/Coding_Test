from itertools import combinations

num = int(input())
result = []
for i in range(1, 11):
    com = list(combinations(range(9,-1,-1),i))

    for ls in com:
        str_num=""
        for j in range(len(ls)):
            str_num += str(ls[j])
        result.append(int(str_num))

result.sort()
if len(result)<=num:
    print(-1)
    exit(0)
else:
    print(result[num])