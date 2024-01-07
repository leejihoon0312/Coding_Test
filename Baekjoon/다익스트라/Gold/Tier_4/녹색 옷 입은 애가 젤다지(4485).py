import heapq, sys

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

loop = 1


def DK(num):
    cost = {}
    pq = []
    heapq.heappush(pq, (graph[0][0], 0, 0))  # 비용, 행, 열

    while pq:
        cur_cost, cur_row, cur_col = heapq.heappop(pq)

        if (cur_row, cur_col) not in cost:
            cost[(cur_row, cur_col)] = cur_cost

            if cur_row == N - 1 and cur_col == N - 1:
                print(f"Problem {num}: {cur_cost}")
                break

            for i in range(4):
                next_row = cur_row + dr[i]
                next_col = cur_col + dc[i]
                if 0 <= next_row < N and 0 <= next_col < N and (next_row, next_col) not in cost:
                    heapq.heappush(pq, (cur_cost + graph[next_row][next_col], next_row, next_col))


while True:
    N = int(input())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    if N == 0:
        break

    DK(loop)
    loop += 1
