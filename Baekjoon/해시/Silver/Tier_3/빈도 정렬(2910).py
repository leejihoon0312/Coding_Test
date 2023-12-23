import sys
length, size = map(int, input().split())


arr = list(map(int, sys.stdin.readline().split()))

count = dict()
order = 0
for num in arr:
    if num in count:
        count[num][0] += 1
    else:
        count[num] = [1, order, num]
        order += 1

for i in sorted(count.values(), key=lambda x:(-x[0], x[1])):
    for j in range(i[0]):
        print(i[2], end=" ")