from itertools import combinations
import sys

size, word = map(int, sys.stdin.readline().split())

arr = list(sys.stdin.readline().split())
j = []
m = []
concat = []
for i in arr:
    if i in ("a", "e", "i", "o", "u"):
        m.append(i)
    else:
        j.append(i)

for i in range(1, len(m) + 1):
    if size - i >= 2:
        com1 = list(combinations(m, i))
        com2 = list(combinations(j, size - i))

        for ls1 in com1:
            for ls2 in com2:
                temp = list(ls1)
                for a in range(len(ls2)):
                    temp.append(ls2[a])
                concat.append(sorted(temp))
result = []
for i in concat:
    result.append("".join(i))
for i in sorted(result):
    print(i)

