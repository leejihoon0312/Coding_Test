from itertools import combinations
import sys

N = row = col = int(input())
graph = []
team = []
minimum = 10**10
for _ in range(row):
    graph.append(list(map(int, sys.stdin.readline().split())))

for num in range(1, N):
    com = list(combinations(range(N), num))

    for pick in com:
        team.append(pick)

for i in range(int(len(team)/2)):
    team_a = list(team[i])
    team_b = list(team[-(i+1)])

    a = 0
    b = 0

    for a1 in team_a:
        for a2 in team_a:
            a += graph[a1][a2]

    for b1 in team_b:
        for b2 in team_b:
            b += graph[b1][b2]

    if minimum > abs(a-b):
        minimum = abs(a - b)
print(minimum)

