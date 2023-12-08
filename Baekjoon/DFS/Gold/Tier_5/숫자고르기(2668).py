from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)

length = int(input())
graph = defaultdict(list)
visited = {}
result = []
for i in range(1, length + 1):
    num = int(input())
    graph[i].append(num)


def dfs(start_num, target_num):
    visited[start_num] = 1

    for next_num in graph[start_num]:
        if next_num not in visited:
            dfs(next_num, target_num)

        if next_num == target_num:
            result.append(target_num)


for i in range(1, length + 1):
    dfs(i, i)
    visited.clear()

print(len(result))
result.sort()
for i in result:
    print(i)
