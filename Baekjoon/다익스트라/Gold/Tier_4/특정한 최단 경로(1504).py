import heapq, sys
from collections import defaultdict
node, edge = map(int, sys.stdin.readline().split())

graph = defaultdict(list)

for _ in range(edge):
    n1, n2, weight = map(int, sys.stdin.readline().split())
    graph[n1].append((weight, n2))
    graph[n2].append((weight, n1))

check_n1, check_n2 = map(int, sys.stdin.readline().split())


def DK(start):
    cost = {}
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if cur_node not in cost:
            cost[cur_node] = cur_cost

            for next_cost, next_node in graph[cur_node]:
                heapq.heappush(pq, (next_cost+cur_cost, next_node))

    if check_n1 not in cost or check_n2 not in cost or node not in cost:
        print(-1)
        exit(0)

    return cost

first = DK(1)

second = DK(check_n1)[check_n2]

third = DK(node)

print(min(first[check_n1]+second+third[check_n2], first[check_n2]+second+third[check_n1], first[check_n1]+second*2+third[check_n1], first[check_n2]+second*2+third[check_n2]))
