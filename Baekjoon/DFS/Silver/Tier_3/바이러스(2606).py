from collections import defaultdict
vertex = int(input())
edge = int(input())
graph = defaultdict(list)
visited ={}
cnt = 0
for i in range(1, edge+1):
    from_v , to_v = map(int, input().split())
    graph[from_v].append(to_v)
    graph[to_v].append(from_v)


def dfs(start_v):
    visited[start_v] = True
    global cnt

    for next_v in graph[start_v]:
        if next_v not in visited:
            dfs(next_v)
            cnt += 1


dfs(1)
print(cnt)