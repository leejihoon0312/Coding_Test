from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 7)
graph = defaultdict(list)
visited = {}
case = dict()
cnt = 1


def dfs(start_v, move):
    visited[start_v] = move
    temp.append(start_v)
    global flag

    for next_v in graph[start_v]:
        if (next_v in visited and abs(visited[next_v] - move) >= 2) or (next_v == start_v):
            flag = False
        if next_v not in visited:
            dfs(next_v, move + 1)


while True:
    temp = []

    result = 0
    vertex, edge = map(int, sys.stdin.readline().split())
    if vertex == edge == 0:
        break

    for _ in range(edge):
        v1, v2 = map(int, sys.stdin.readline().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    for v in range(1, vertex + 1):
        if v not in visited:
            flag = True
            dfs(v, 1)
            if flag:
                result += 1

    case[cnt] = result
    graph.clear()
    visited.clear()

    cnt += 1

for i in case:
    if case[i] == 0:
        print(f'Case {i}: No trees.')
    elif case[i] == 1:
        print(f'Case {i}: There is one tree.')
    else:
        print(f'Case {i}: A forest of {case[i]} trees.')
