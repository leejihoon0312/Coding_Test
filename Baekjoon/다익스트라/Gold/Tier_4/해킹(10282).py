import heapq, sys
from collections import defaultdict

case = int(input())


def DK():
    cost = {}
    pq = []
    heapq.heappush(pq, (0, start_node))
    depth = 0
    max_cost = 0

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if cur_node not in cost:

            cost[cur_node] = cur_cost
            depth += 1
            max_cost = max(max_cost, cur_cost)

            for next_cost, next_node in graph[cur_node]:
                heapq.heappush(pq, (next_cost + cur_cost, next_node))

    return depth, max_cost


for _ in range(case):
    node, edge, start_node = map(int, sys.stdin.readline().split())

    graph = defaultdict(list)

    for _ in range(edge):
        to_n, from_n, weight = map(int, sys.stdin.readline().split())
        graph[from_n].append((weight, to_n))

    depth, max_cost = DK()

    print(depth, end=" ")
    print(max_cost)
