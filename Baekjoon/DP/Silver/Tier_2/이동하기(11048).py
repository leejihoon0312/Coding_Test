import sys
N, M = map(int, input().split())

graph = [[0]*(M+1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]


for r in range(1, N+1):
    for c in range(1, M+1):
        graph[r][c] = max(graph[r-1][c], graph[r][c-1], graph[r-1][c-1]) + graph[r][c]

print(graph[N][M])
