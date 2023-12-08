import sys
sys.setrecursionlimit(10**6)

row = col = int(input())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]

# (수직, 수평, 대각)
dr = [1, 0, 1]
dc = [0, 1, 1]
cnt = 0
def dfs(r, c, prev):
    global cnt
    if r == c == row-1:
        cnt += 1
    for i in range(3):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0<= next_r<row and 0<=next_c<col and (prev == i or i == 2 or prev == 2) and graph[next_r][next_c] ==0:
            if i ==2 and graph[r+1][c]==0 and graph[r][c+1]==0 and graph[r+1][c+1]==0:
                dfs(next_r, next_c, i)
            elif i!=2:
                dfs(next_r, next_c, i)





dfs(0, 1, 1)

print(cnt)
