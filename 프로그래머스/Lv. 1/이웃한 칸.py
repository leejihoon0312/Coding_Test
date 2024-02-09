def solution(board, h, w):
    answer = 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):
        next_r = h + dr[i]
        next_c = w + dc[i]
        if 0 <= next_r < len(board) and 0 <= next_c < len(board) and board[next_r][next_c] == board[h][w]:
            answer += 1

    return answer