N = int(input())

graph = [[0] * 4] + [[0] * 4 for _ in range(N)]

graph[1][1] = 1
graph[1][2] = 1
graph[1][3] = 1


def DP():
    for i in range(2, N + 1):
        graph[i][1] = (graph[i - 1][2] + graph[i - 1][3]) % 9901
        graph[i][2] = (graph[i - 1][1] + graph[i - 1][3]) % 9901
        graph[i][3] = (graph[i - 1][1] + graph[i - 1][2] + graph[i - 1][3]) % 9901

    return sum(graph[N])


print(DP()%9901)
