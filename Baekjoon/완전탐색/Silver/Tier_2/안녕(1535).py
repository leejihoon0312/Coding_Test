from itertools import combinations
import sys

vertex = int(input())
lose = list(map(int, sys.stdin.readline().split()))
joy = list(map(int, sys.stdin.readline().split()))
max_happy = 0

for i in range(1, vertex+1):
    c = combinations(range(vertex), i)

    for ls in c:
        hp = 100
        happy = 0
        for i in ls:
            hp -= lose[i]
            happy += joy[i]

        if hp>0:
            max_happy = max(max_happy, happy)

print(max_happy)
