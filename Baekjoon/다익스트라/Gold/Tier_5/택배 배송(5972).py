import heapq
from collections import defaultdict

node, edge = map(int, input().split())

cow_road = defaultdict(list)

for _ in range(edge):
    start, end, weight = map(int, input().split())
    cow_road[start].append((weight, end))
    cow_road[end].append((weight, start))


def DK():
    cost = {}
    pq = []
    heapq.heappush(pq, (0, 1))

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if cur_node not in cost:
            cost[cur_node] = cur_cost

            for next_cost, next_node in cow_road[cur_node]:
                heapq.heappush(pq, (next_cost + cur_cost, next_node))

    print(cost[node])


DK()
