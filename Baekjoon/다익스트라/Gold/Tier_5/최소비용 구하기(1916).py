import heapq, sys
from collections import defaultdict

node = int(input())
edge = int(input())

bus = defaultdict(list)

for _ in range(edge):
    start, finish, weight = map(int, sys.stdin.readline().split())
    bus[start].append((weight, finish))

start_num, finish_num = map(int, sys.stdin.readline().split())


def DK(start, end):
    cost = dict()
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if cur_node not in cost:
            cost[cur_node] = cur_cost
            for next_cost, next_node in bus[cur_node]:
                next_cost += cur_cost
                heapq.heappush(pq, (next_cost, next_node))

    print(cost[end])


DK(start_num, finish_num)
