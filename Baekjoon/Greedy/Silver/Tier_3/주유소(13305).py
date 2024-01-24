import sys

N = int(input())

road_length = list(map(int, sys.stdin.readline().split()))
oil_cost = list(map(int, sys.stdin.readline().split()))

oil_cost.pop()

result = 0
min_oil_cost = oil_cost[0]
length = road_length[0]

for i in range(1, N - 1):
    if min_oil_cost <= oil_cost[i]:
        length += road_length[i]
    else:
        result += (min_oil_cost * length)
        min_oil_cost = oil_cost[i]
        length = road_length[i]

print(result + (min_oil_cost * length))
