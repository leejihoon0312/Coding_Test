import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
vertex, praise = map(int, input().split())

mento = list(map(int, sys.stdin.readline().split()))
graph = defaultdict(list)
weight_list = defaultdict(list)
result = [0] * (vertex + 1)
for i in range(1, len(mento)):
    graph[mento[i]].append(i + 1)

for i in range(praise):
    mentee, weight = map(int, sys.stdin.readline().split())
    weight_list[mentee].append(weight)


def dfs(start_v, cur_weight):
    result[start_v] = cur_weight
    for next_v in graph[start_v]:
        if next_v in weight_list:
            total = 0
            for i in weight_list[next_v]:
                total += i
            dfs(next_v, cur_weight + total)
        else:
            dfs(next_v, cur_weight)


dfs(1, 0)

for i in range(1, vertex + 1):
    print(result[i], end=" ")
