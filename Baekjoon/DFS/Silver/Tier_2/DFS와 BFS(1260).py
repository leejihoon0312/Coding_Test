from collections import defaultdict
from collections import deque
vertex, edge, start = map(int, input().split())
graph = defaultdict(list)
visited_dfs = {}
visited_bfs = {}
for i in range(edge):
    from_v, to_v = map(int, input().split())
    graph[from_v].append(to_v)
    graph[to_v].append(from_v)
for i in range(1, vertex+1):
    graph[i].sort()

def dfs(start_v):
        visited_dfs[start_v] = True
        for next_v in graph[start_v]:
            if next_v not in visited_dfs:
                dfs(next_v)

def bfs(start_v):
    visited_bfs[start_v] = True
    q = deque()
    q.append(graph[start_v])
    while q:
        near_list = q.popleft()

        for next_v in near_list:
            if next_v not in visited_bfs:
                q.append(graph[next_v])
                visited_bfs[next_v] = True


dfs(start)
for i in visited_dfs.keys():
    print(i,end=" ")
print()
bfs(start)
for i in visited_bfs.keys():
    print(i,end=" ")