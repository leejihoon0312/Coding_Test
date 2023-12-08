row, col = map(int, input().split())
tile = []
visited = [[False] * col for _ in range(row)]
cnt = 0
for _ in range(row):
    tile.append(list(input()))


def dfs(r, c):
    visited[r][c] = True
    if tile[r][c] == "|":
        if r + 1 < row and not visited[r + 1][c] and tile[r+1][c] == "|":
            dfs(r + 1, c)

    else:
        if c + 1 < col and not visited[r][c + 1] and tile[r][c+1] == "-":
            dfs(r, c + 1)




for cur_row in range(row):
    for cur_col in range(col):
        if not visited[cur_row][cur_col]:
            dfs(cur_row, cur_col)
            cnt += 1



print(cnt)
