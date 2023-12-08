from itertools import combinations

food = int(input())
arr = []
minimum = 10 ** 10
for _ in range(food):
    s, b = map(int, input().split())
    arr.append((s, b))

for i in range(1, food + 1):
    c = combinations(arr, i)

    for ls in c:
        s = 1
        b = 0
        for j in range(len(ls)):
            cur_s, cur_b = ls[j]
            s *= cur_s
            b += cur_b
        minimum = min(minimum, abs(s - b))

print(minimum)
