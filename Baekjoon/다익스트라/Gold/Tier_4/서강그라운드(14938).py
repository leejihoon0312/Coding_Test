import heapq, sys
from collections import defaultdict

node, area_length, edge = map(int, sys.stdin.readline().split())

item = list(map(int, sys.stdin.readline().split()))

graph = defaultdict(list)

max_item = 0

for _ in range(edge):
    n1, n2, weight = map(int, sys.stdin.readline().split())
    graph[n1].append((weight, n2))
    graph[n2].append((weight, n1))


def DK(start):
    cost = {}
    pq = []
    heapq.heappush(pq, (0, start))
    temp_max_item = 0
    global max_item

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if cur_node not in cost:
            cost[cur_node] = cur_cost
            temp_max_item += item[cur_node - 1]

            for next_cost, next_node in graph[cur_node]:
                if next_cost + cur_cost <= area_length:
                    heapq.heappush(pq, (next_cost + cur_cost, next_node))

    max_item = max(temp_max_item, max_item)


for node_num in range(1, node + 1):
    DK(node_num)

print(max_item)
