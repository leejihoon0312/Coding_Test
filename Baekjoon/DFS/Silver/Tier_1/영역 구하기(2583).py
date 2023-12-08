import sys
sys.setrecursionlimit(10**6)

row, col, square = map(int, input().split())
graph = []
square_area = []
visited = []
result = []
for i in range(row):
    graph.append([0]*col)
    visited.append([0]*col)
for i in range(square):
    lt_c, lt_r, rb_c, rb_r = map(int, input().split())
    square_area.append((lt_c, lt_r, rb_c-1, rb_r-1))


for area in square_area:
    lt_c, lt_r, rb_c, rb_r = area
    for cur_row in range(lt_r, rb_r+1):
        for cur_col in range(lt_c, rb_c+1):
            graph[cur_row][cur_col] = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    visited[r][c] = 1
    global count
    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0<=next_r<row and 0<= next_c<col and visited[next_r][next_c] == 0 and graph[next_r][next_c] ==0:
            count += 1
            dfs(next_r, next_c)


for cur_row in range(row):
    for cur_col in range(col):
        if visited[cur_row][cur_col] ==0 and graph[cur_row][cur_col] ==0:
            count = 1
            dfs(cur_row, cur_col)
            result.append(count)

result.sort()
print(len(result))
for i in result:
    print(i, end=" ")