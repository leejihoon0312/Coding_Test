from collections import Counter
import sys

case = int(input())
result = []
for i in range(case):
    number = int(input())
    closet = []
    for _ in range(number):
        name, category = sys.stdin.readline().strip().split()
        closet.append(category)
    closet = dict(Counter(closet))
    init = 1
    for key in closet.keys():
        init *= (closet[key]+1)
    result.append(init - 1)

for i in result:
    print(i)
