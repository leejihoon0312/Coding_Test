from collections import deque

row, col = map(int,input().split(" "))
matrix = []
minimum = 700
for _ in range(row):
    matrix.append(list(map(int, input().split(" "))))


dx = [1, 1, 1]
dy = [-1, 0, 1]


#(행 정보, 열 정보, 이전에 어떻게 왔는지, 총합)
q = deque()
for i in range(col):
    q.append((0, i , -1, 0))
while q:
    cur_row, cur_col, direction, total = q.popleft()
    if cur_row == (row-1):
        minimum = min(matrix[cur_row][cur_col] + total, minimum)
        continue
    for i in range(3):
        next_row = cur_row + dx[i]
        next_col = cur_col + dy[i]
        if 0 <= next_row < row and 0 <= next_col < col and direction != i:
            q.append((next_row, next_col, i, matrix[cur_row][cur_col] + total))

print(minimum)
