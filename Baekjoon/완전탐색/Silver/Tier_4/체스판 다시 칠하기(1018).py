row, col = map(int, input().split(" "))
board = []
result = []
cnt = 0
for _ in range(row):
    board.append(list(input()))

for i in range(row - 8 + 1):
    for j in range(col - 8 + 1):
        b_start = 0
        w_start = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k+l)%2==0:
                    if board[k][l] == 'B':
                        b_start+=0
                        w_start+=1
                    else:
                        b_start += 1
                        w_start += 0
                else:
                    if board[k][l] == 'B':
                        b_start+=1
                        w_start+=0
                    else:
                        b_start += 0
                        w_start += 1
        result.append(min(b_start,w_start))


print(min(result))
