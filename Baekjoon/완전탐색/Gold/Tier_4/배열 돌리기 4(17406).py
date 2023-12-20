from itertools import permutations
import sys, copy

row, col, K = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

minimum = 10 ** 10


def rotate(s_r, e_r, s_c, e_c, g):
    # 오른쪽으로 밀기
    for i in range(s_c, e_c):
        copy_graph[s_r][i + 1] = g[s_r][i]

    # 아래쪽으로 밀기
    for i in range(s_r, e_r):
        copy_graph[i + 1][e_c] = g[i][e_c]

    # 왼쪽으로 밀기
    for i in range(e_c, s_c, -1):
        copy_graph[e_r][i - 1] = g[e_r][i]

    # 위쪽으로 밀기
    for i in range(e_r, s_r, -1):
        copy_graph[i - 1][s_c] = g[i][s_c]


for per_ls in list(permutations(arr, K)):

    copy_graph = [array[:] for array in graph]
    for order in list(per_ls):
        r, c, s = order

        start_r = r - s - 1
        end_r = r + s + -1
        start_c = c - s - 1
        end_c = c + s - 1

        for num in range(int((end_r - start_r + 1) / 2)):
            rotate(start_r + num, end_r - num, start_c + num, end_c - num, [array[:] for array in copy_graph])

    for g in copy_graph:
        minimum = min(minimum, sum(g))

print(minimum)
