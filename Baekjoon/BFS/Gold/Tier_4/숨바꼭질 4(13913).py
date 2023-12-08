from collections import deque, defaultdict

path = dict()

subin, brother = map(int, input().split())

graph = [0] * 100001
visited = [0] * 100001
dist = 0
result = []
dc = [-1, 1, 2]


def bfs(start_num):
    q = deque()
    q.append((start_num, 0))
    visited[start_num] = 1
    global dist
    while q:
        cur_num, cur_dist = q.popleft()

        if cur_num == brother:
            dist = cur_dist
            break

        for i in range(3):
            if i == 2:
                next_num = cur_num * dc[i]
            else:
                next_num = cur_num + dc[i]
            if 0 <= next_num <= 100000 and visited[next_num] == 0:
                visited[next_num] = 1
                path[next_num] = cur_num
                q.append((next_num, cur_dist + 1))


bfs(subin)
if dist == 0:
    print(dist)
    print(subin)
else:
    from_num = path[brother]
    result.append(brother)
    print(dist)
    while True:
        result.append(from_num)
        if from_num != subin:
            from_num = path[from_num]
        else:
            break
    result.reverse()
    for i in range(len(result)):
        print(result[i], end=" ")
