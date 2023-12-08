from collections import deque
row = col = int(input())

graph = [ list(map(int, input().split()))   for _ in range(row)]
visited = [ [0]*col for _ in range(row)]



def bfs(r, c):
    q = deque()
    q.append((r,c))
    while q:
        cur_r, cur_c = q.popleft()

        if cur_r == cur_c == row-1:
            print("HaruHaru")
            exit(0)

        dr = [graph[cur_r][cur_c], 0]
        dc = [0, graph[cur_r][cur_c]]


        for i in range(2):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]

            if 0<=next_r<row and 0<=next_c<col and visited[next_r][next_c]==0:
                visited[next_r][next_c] = 1
                q.append((next_r, next_c))



bfs(0, 0)

print("Hing")