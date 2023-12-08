from itertools import combinations
times, target = map(int, input().split(" "))
num_list = list(map(int, input().split(" ")))
cnt = 0

for i in range(1,times+1):
    select = combinations(num_list,i)
    for j in select:
        if sum(j) == target:
            cnt += 1
print(cnt)