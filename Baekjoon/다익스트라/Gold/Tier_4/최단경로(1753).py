import heapq, sys
from collections import defaultdict

vertex, edge = map(int, sys.stdin.readline().split())
start = int(input())
cost = {}
graph = defaultdict(list)

for _ in range(edge):
    v1, v2, weight = map(int, sys.stdin.readline().split())
    graph[v1].append((weight, v2))


def DK():
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur_vertex = heapq.heappop(pq)

        if cur_vertex not in cost:
            cost[cur_vertex] = cur_cost
            for next_cost, next_vertex in graph[cur_vertex]:
                heapq.heappush(pq, (next_cost + cur_cost, next_vertex))


DK()

for i in range(1, vertex + 1):
    if i in cost:
        print(cost[i])
    else:
        print("INF")
