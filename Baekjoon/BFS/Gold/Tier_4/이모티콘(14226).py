from collections import deque

end = int(input())

graph = [2000] * 1001
visited = [0] * 1001
start = 1
copy = [0] * 1001

def bfs(start_num):
    q = deque()
    clip_cnt = 0
    sec = 0
    q.append((start_num, sec, clip_cnt))
    # visited[start_num] = 1
    graph[start_num] = sec

    while q:
        cur_num, cur_sec, cur_clip_cnt = q.popleft()
        # visited[cur_num] = 1

        # if cur_num == end:
        #     return


        for i in range(3):
            if i == 0 and copy[cur_num] == 0 and cur_num != 0:
                q.append((cur_num, cur_sec+1, cur_num))
                copy[cur_num] = 1

            if i == 1 and cur_clip_cnt>0 and 0<=cur_num + cur_clip_cnt<1001 and graph[cur_num + cur_clip_cnt] >= cur_sec + 1 :
                graph[cur_num + cur_clip_cnt] = cur_sec + 1
                q.append((cur_num + cur_clip_cnt, cur_sec + 1, cur_clip_cnt))

            if i == 2 and 0<=cur_num - 1<1001  and graph[cur_num - 1] >= cur_sec + 1 :
                graph[cur_num - 1] = cur_sec + 1
                q.append((cur_num - 1, cur_sec + 1, cur_clip_cnt))



        # for i in range(3):
        #     if i == 0:
        #         q.append((cur_num, cur_sec+1, cur_num))
        #
        #     if i == 1 and cur_clip_cnt>0 and 0<=cur_num + cur_clip_cnt<1001 and graph[cur_num + cur_clip_cnt] >= cur_sec + 1 and visited[cur_num+ cur_clip_cnt] ==0:
        #         graph[cur_num + cur_clip_cnt] = cur_sec + 1
        #         q.append((cur_num + cur_clip_cnt, cur_sec + 1, cur_clip_cnt))
        #     if i == 2 and 0<=cur_num - 1<1001 and graph[cur_num - 1] >= cur_sec+ 1 and visited[cur_num -1] ==0:
        #         graph[cur_num - 1] = cur_sec + 1
        #         q.append((cur_num - 1, cur_sec + 1, cur_clip_cnt))

bfs(start)

print(graph[end])
