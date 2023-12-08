from collections import deque
height, start, end, up, down = map(int, input().split())

arr = [0]*height
visited = [0]*height


d_idx = [up, -down]

def bfs(start_idx):
    q = deque()
    q.append((start_idx, 0))
    visited[start_idx] = 1
    arr[start_idx] = 0

    while q:
        cur_idx, cnt = q.popleft()

        for i in range(2):
            next_idx = cur_idx + d_idx[i]
            if 0<=next_idx<height and visited[next_idx] ==0:
                visited[next_idx] = 1
                arr[next_idx] = cnt + 1
                q.append((next_idx, cnt + 1))

bfs(start-1)

if visited[end-1] == 0:
    print('use the stairs')
else:
    print(arr[end-1])