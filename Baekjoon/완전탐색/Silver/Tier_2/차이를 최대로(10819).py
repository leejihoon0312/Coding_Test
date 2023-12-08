from itertools import permutations

size = int(input())

arr = list(map(int, input().split()))
max = 0

for sub in permutations(arr,size):
    temp = 0
    for i in range(1, size):
        temp += abs(sub[i-1] - sub[i])
    if temp > max:
        max = temp

print(max)        