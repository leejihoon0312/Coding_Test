import heapq, sys
from collections import defaultdict

node, edge = map(int, sys.stdin.readline().split())

graph = defaultdict(list)

for _ in range(edge):
    n1, n2, weight = map(int, sys.stdin.readline().split())
    graph[n1].append((weight, n2))
    graph[n2].append((weight, n1))

start, end = map(int, sys.stdin.readline().split())

def DK():
    cost = {}
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if cur_node not in cost:
            cost[cur_node] = cur_cost
            if cur_node == end:
                print(cost[cur_node])
                exit(0)
            for next_cost, next_node in graph[cur_node]:
                heapq.heappush(pq, (next_cost+cur_cost, next_node))

DK()
