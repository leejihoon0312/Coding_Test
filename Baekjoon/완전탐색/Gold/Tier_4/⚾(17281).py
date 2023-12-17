from itertools import permutations
import sys
max_score = 0
inning = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(inning)]
for order in list(permutations(range(1, 9), 8)):
    order = list(order)
    order = order[:3] + [0] + order[3:]
    order_idx = 0
    last_batter = order[order_idx]
    score = 0
    for inning_num in range(inning):
        out_count = 0
        base1 = 0
        base2 = 0
        base3 = 0
        while True:
            if graph[inning_num][last_batter] == 1:
                if base3 == 1:
                    score += 1
                    base3 = 0
                if base2 == 1:
                    base3 = 1
                    base2 = 0
                if base1 == 1:
                    base2 = 1
                    base1 = 0
                if base1 == 0:
                    base1 = 1

            elif graph[inning_num][last_batter] == 2:
                if base3 == 1:
                    score += 1
                    base3 = 0
                if base2 == 1:
                    score += 1
                    base2 = 0
                if base1 == 1:
                    base3 = 1
                    base1 = 0
                if base2 == 0:
                    base2 = 1

            elif graph[inning_num][last_batter] == 3:
                if base3 == 1:
                    score += 1
                    base3 = 0
                if base2 == 1:
                    score += 1
                    base2 = 0
                if base1 == 1:
                    score += 1
                    base1 = 0
                if base3 == 0:
                    base3 = 1

            elif graph[inning_num][last_batter] == 4:
                score += base3 + base2 + base1 + 1
                base1 = 0
                base2 = 0
                base3 = 0

            elif graph[inning_num][last_batter] == 0:
                out_count += 1

            order_idx = (order_idx + 1) % 9
            last_batter = order[order_idx]

            if out_count == 3:
                break


    max_score = max(max_score, score)

print(max_score)