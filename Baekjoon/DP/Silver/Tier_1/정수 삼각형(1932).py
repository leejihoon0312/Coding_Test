import sys

N = int(input())

graph = [0] + [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def DP():
    for i in range(N-1, 0, -1):
        for j in range(i):
            graph[i][j] = max(graph[i + 1][j], graph[i + 1][j + 1]) + graph[i][j]

    return graph[1][0]


print(DP())
