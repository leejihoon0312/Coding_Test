import sys

N = int(input())

mp, mf, ms, mv = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

min_cost = 10 ** 5
ingredient_arr = []


def backtracking(ingredient_num, p, f, s, v, cost, arr):
    global min_cost, ingredient_arr

    if p >= mp and f >= mf and s >= ms and v >= mv and cost < min_cost:
        min_cost = cost
        ingredient_arr = arr[:]
        return

    if len(arr) == N:
        print(-1)
        exit(0)

    for number in range(ingredient_num + 1, N):
        arr.append(number)
        backtracking(number, p + graph[number][0], f + graph[number][1], s + graph[number][2], v + graph[number][3],
                     cost + graph[number][4], arr)
        arr.pop()


for num in range(N):
    backtracking(num, graph[num][0], graph[num][1], graph[num][2], graph[num][3], graph[num][4], [num])

if min_cost == 10 ** 5:
    print(-1)
else:
    print(min_cost)
    for i in ingredient_arr:
        print(i + 1, end=" ")
