from collections import deque
import sys

vertex = int(input())

graph = list(map(int, sys.stdin.readline().split()))

start_idx = int(input()) - 1
visited = {}
cnt = 1


def bfs(idx):
    q = deque()
    q.append(idx)
    global cnt, graph
    visited[start_idx] = True

    while q:
        cur_idx = q.popleft()

        d_idx = [-graph[cur_idx], graph[cur_idx]]

        for i in range(2):
            next_idx = cur_idx + d_idx[i]

            if 0 <= next_idx < vertex and next_idx not in visited:
                q.append(next_idx)
                visited[next_idx] = True
                cnt += 1


bfs(start_idx)
print(cnt)
