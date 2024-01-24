
N = int(input())

rope = [int(input()) for _ in range(N)]

rope.sort()

max_weight = 0
for order in range(N):
    max_weight = max(max_weight, rope[order]*(N-order))
print(max_weight)



