from itertools import combinations
import sys

member = row = col = int(input())
diff = 10*10
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
arr = []
ls = combinations(range(member), int(member/2))

for team in ls:
    temp = 0
    for i in team:
        for j in team:
            temp += graph[i][j]

    arr.append(temp)

for i in range(int(len(arr)/2)):
    diff = min(abs(arr[i] - arr[-(i+1)]), diff)

print(diff)