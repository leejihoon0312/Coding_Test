from collections import deque

start, end = map(int, input().split())
visited = {}


def bfs(start_num, end_num):
    q = deque()
    q.append((start_num, 1))
    visited[start_num] = True
    while q:
        cur_num, cnt = q.popleft()

        if cur_num == end_num:
            print(cnt)
            exit(0)

        for next_num in [cur_num * 2, int(str(cur_num) + "1")]:
            if next_num not in visited and next_num <= end_num:
                visited[next_num] = True
                q.append((next_num, cnt + 1))


bfs(start, end)
print(-1)
