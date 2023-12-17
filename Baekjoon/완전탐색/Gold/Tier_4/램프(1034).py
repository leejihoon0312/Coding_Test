import sys

row, col = map(int, input().split())
graph = []
zero_cnt = dict()

for i in range(row):
    zero_cnt[i] = 0
    ls = list(map(int, sys.stdin.readline().strip()))
    for j in range(len(ls)):
        if ls[j] == 0:
            zero_cnt[i] += 1
    graph.append(ls)

times = int(input())
location = []

for r in range(row):
    if zero_cnt[r] % 2 == 0 and times % 2 == 0 and zero_cnt[r] <= times:
        location.append(r)
    elif zero_cnt[r] % 2 != 0 and times % 2 != 0 and zero_cnt[r] <= times:
        location.append(r)

word = dict()
for loc in location:
    ls = list(map(str, graph[loc]))
    str_num = "".join(ls)
    if str_num in word:
        word[str_num] += 1
    else:
        word[str_num] = 1


if len(word) == 0:
    print(0)
else:
    print(max(word.values()))

