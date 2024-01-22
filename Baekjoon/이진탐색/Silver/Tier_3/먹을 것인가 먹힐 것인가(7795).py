import sys
from bisect import bisect_left
T = int(input())


for _ in range(T):
    number_of_A, number_of_B = map(int, input().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    B.sort()

    result = 0
    for number in A:
        result += bisect_left(B, number)

    print(result)
