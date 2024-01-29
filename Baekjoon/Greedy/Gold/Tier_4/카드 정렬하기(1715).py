import heapq

N = int(input())

pq = [int(input()) for _ in range(N)]

pq.sort()

if N == 1:
    print(0)
    exit(0)

result = 0
while len(pq) >= 2:
    num1 = heapq.heappop(pq)
    num2 = heapq.heappop(pq)

    result += num1 + num2

    heapq.heappush(pq, num1 + num2)

print(result)
