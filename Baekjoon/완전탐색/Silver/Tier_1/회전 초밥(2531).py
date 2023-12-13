import sys

vertex, number, link, coupon = map(int, input().split())
max_len = 0
graph = [int(sys.stdin.readline()) for _ in range(vertex)]
graph = graph + graph

for i in range(vertex):

    s = set(graph[i:i + link])
    s.add(coupon)

    if len(s) > max_len:
        max_len = len(s)

print(max_len)
