import heapq, sys

row, col = map(int, sys.stdin.readline().split())

junan_row, junan_col, suspect_row, suspect_col = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(row)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def DK():
    cost = {}
    pq = []
    heapq.heappush(pq, (0, junan_row - 1, junan_col - 1))

    while pq:
        cur_cost, cur_row, cur_col = heapq.heappop(pq)

        if (cur_row, cur_col) not in cost:
            cost[(cur_row, cur_col)] = cur_cost

            for i in range(4):
                next_row = cur_row + dr[i]
                next_col = cur_col + dc[i]
                if 0 <= next_row < row and 0 <= next_col < col:
                    if graph[next_row][next_col] == '1':
                        heapq.heappush(pq, (cur_cost + 1, next_row, next_col))
                    elif graph[next_row][next_col] == '0':
                        heapq.heappush(pq, (cur_cost, next_row, next_col))
                    elif graph[next_row][next_col] == '#':
                        print(cur_cost + 1)
                        exit(0)


DK()
