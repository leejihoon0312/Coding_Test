from collections import deque

start, end = map(int, input().split())

visited = {}


def bfs(start_num, end_num):
    q = deque()
    q.append((start_num,0))
    visited[start_num] = True

    while q:
        cur_num, cnt = q.popleft()

        if cur_num == end_num:
            print(cnt)
            exit(0)

        if cur_num*2 <= end_num and cur_num*2 not in visited:
            visited[cur_num*2] = True
            q.append((cur_num*2, cnt+1))
        if cur_num + 1 <= end_num and cur_num+1 not in visited:
            visited[cur_num + 1] = True
            q.append((cur_num + 1, cnt + 1))



bfs(start, end)