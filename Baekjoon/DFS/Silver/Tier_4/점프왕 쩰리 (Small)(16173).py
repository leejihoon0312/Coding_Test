row = col = int(input())
matrix = []
for _ in range(row):
    matrix.append(list(map(int, input().split())))
visited =[[False]*row for _ in range(row)]
def recursion(r, c):
    visited[r][c] = True


    if r == c == (row-1):
        print("HaruHaru")
        exit(0)

    if c + matrix[r][c] < col and not visited[r][c + matrix[r][c]]:
        recursion(r, c + matrix[r][c])
    if r + matrix[r][c] < row and not visited[r + matrix[r][c]][c]:
        recursion(r + matrix[r][c], c)

recursion(0, 0)
print("Hing")