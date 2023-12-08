from itertools import combinations
import sys

sys.setrecursionlimit(10 ** 7)
vertex = int(sys.stdin.readline())
graph = dict()
populations = list(map(int, sys.stdin.readline().split()))
populations.insert(0, 0)
comb = []
difference = 1001

visited = {}

for i in range(1, vertex + 1):
    link = list(map(int, sys.stdin.readline().split()))
    del link[0]
    graph[i] = link

for i in range(1, int(vertex / 2) + 1):
    c = combinations(range(1, vertex + 1), i)
    for j in c:
        comb.append(j)


def dfs(start_v, section):
    visited[start_v] = 1

    for next_v in graph[start_v]:
        if next_v not in visited and next_v in section:
            dfs(next_v, section)


for i in comb:

    section_a = []
    section_b = []
    section_a_num = 0
    section_b_num = 0
    flag = True
    for j in range(1, vertex + 1):
        if j in i:
            section_a.append(j)
            section_a_num += populations[j]
        elif j not in i:
            section_b.append(j)
            section_b_num += populations[j]
    dfs(section_a[0], section_a)
    dfs(section_b[0], section_b)

    for k in range(1, vertex + 1):
        if k not in visited:
            flag = False

    if flag:
        if difference > abs(section_a_num - section_b_num):
            difference = abs(section_a_num - section_b_num)

    visited.clear()

if difference == 1001:
    print(-1)
else:
    print(difference)
