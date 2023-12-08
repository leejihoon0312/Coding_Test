from collections import deque

row = col = 10

ladder_num, snake_num = map(int, input().split())

graph = [0] * 101
visited = [0] * 101
ladder = dict()
snake = dict()
for _ in range(ladder_num):
    from_num, to_num = map(int, input().split())
    ladder[from_num] = to_num

for _ in range(snake_num):
    from_num, to_num = map(int, input().split())
    snake[from_num] = to_num


def bfs(start):
    q = deque()
    q.append((start, 0))
    visited[start] = 1

    while q:
        cur_idx, dist = q.popleft()

        if cur_idx == 100:
            print(dist)
            exit(0)

        for i in range(1, 7):
            next_idx = cur_idx + i
            if 1 <= next_idx <= 100 and visited[next_idx] == 0:

                if next_idx in ladder:
                    next_idx = ladder[next_idx]
                if next_idx in snake:
                    next_idx = snake[next_idx]

                if graph[next_idx] == 0:
                    visited[next_idx] = 1
                    graph[next_idx] = dist + 1
                    q.append((next_idx, dist + 1))


bfs(1)
