import sys

N, M =map(int, sys.stdin.readline().split())

graph = [[0]*(N+1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for r in range(1, N+1):
    for c in range(1, N+1):
        graph[r][c] = graph[r][c-1] + graph[r][c] + graph[r-1][c] - graph[r-1][c-1]


for _ in range(M):
    s_r, s_c, e_r,e_c = map(int, sys.stdin.readline().split())
    print(graph[e_r][e_c] - graph[s_r-1][e_c] - graph[e_r][s_c-1] + graph[s_r-1][s_c-1])