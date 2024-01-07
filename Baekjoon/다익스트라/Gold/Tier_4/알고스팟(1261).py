import heapq, sys

col, row = map(int, input().split())

graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(row)]
visited = [[0] * col for _ in range(row)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def DK():
    cost = {}
    pq = []
    heapq.heappush(pq, (0, 0, 0))  # 가중치 , 행, 열

    while pq:
        cur_cost, cur_row, cur_col = heapq.heappop(pq)

        if (cur_row, cur_col) not in cost:
            cost[(cur_row, cur_col)] = cur_cost
            if cur_row == row - 1 and cur_col == col - 1:
                print(cur_cost)
                exit(0)

            for i in range(4):
                next_row = cur_row + dr[i]
                next_col = cur_col + dc[i]

                if 0 <= next_row < row and 0 <= next_col < col and (next_row, next_col) not in cost:
                    heapq.heappush(pq, (cur_cost + graph[next_row][next_col], next_row, next_col))


DK()
