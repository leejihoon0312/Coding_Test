from bisect import bisect_left, bisect_right

N, H = map(int, input().split())

from_bottom = [] # 석순
from_top = []    # 종유석

destroy = 10**10
count = 0

for i in range(1, N+1):
    if i%2 == 0:
        from_top.append(int(input()))
    else:
        from_bottom.append(int(input()))
from_top.sort()
from_bottom.sort()

for height in range(1, H+1):
    obj = 0
    obj += len(from_bottom) - bisect_left(from_bottom, height)
    obj += len(from_top) - bisect_left(from_top, H-height+1)

    if destroy>obj:
        count = 1
        destroy = obj
    elif destroy==obj:
        count+=1

print(f"{destroy} {count}")
