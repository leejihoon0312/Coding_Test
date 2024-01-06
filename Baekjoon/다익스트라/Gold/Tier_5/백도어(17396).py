import heapq,sys
from collections import defaultdict
node, edge = map(int, sys.stdin.readline().split())

eyesight = list(map(int, sys.stdin.readline().split()))

nexus = defaultdict(list)

for _ in range(edge):
    n1, n2, weight = map(int, sys.stdin.readline().split())
    nexus[n1].append((weight, n2))
    nexus[n2].append((weight, n1))

def DK():
    cost = {}
    pq = []
    heapq.heappush(pq, (0,0)) # 가중치, 노드

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if cur_node not in cost:
            cost[cur_node] = cur_cost

            for next_cost, next_node in nexus[cur_node]:
                if eyesight[next_node] == 0 or next_node == node-1 and next_node not in cost:
                    heapq.heappush(pq, (next_cost+cur_cost, next_node))

    if node-1 in cost:
        print(cost[node-1])
    else:
        print(-1)

DK()