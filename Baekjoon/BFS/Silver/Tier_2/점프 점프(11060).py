from collections import deque
import sys
col = int(input())

arr = list(map(int, sys.stdin.readline().split()))
visited ={}


def bfs(start):
    q = deque()
    q.append((start, 0))
    visited[start] = True

    while q:
        cur_idx, cnt = q.popleft()

        if cur_idx == col-1:
            print(cnt)
            exit(0)

        for move_cnt in range(1, arr[cur_idx]+1):
            next_idx = cur_idx+move_cnt
            if next_idx not in visited and next_idx<col:
                visited[next_idx] = True
                q.append((next_idx, cnt+1))


bfs(0)
print(-1)