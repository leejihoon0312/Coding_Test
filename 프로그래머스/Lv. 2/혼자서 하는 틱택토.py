# 실패 조건
# 1. o와 x의 차이가 2개 이상일때
# 2. o가 x보다 작을때
# 3. o빙고가 만들어질때 x의 갯수가 o와 같을때
# 4. x빙고가 만들어질때 o의 갯수가 x보다 1클때
def bingo(board, ox):
    # 행
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == ox:
            return True
    # 열
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == ox:
            return True
            # 대각
    if board[0][0] == board[1][1] == board[2][2] == ox:
        return True
    if board[0][2] == board[1][1] == board[2][0] == ox:
        return True

    return False


def solution(board):
    answer = 1

    circle = 0
    cross = 0
    isCircleBingo = bingo(board, "O")
    isCrossBingo = bingo(board, "X")
    for r in range(3):
        for c in range(3):
            if board[r][c] == "O":
                circle += 1
            if board[r][c] == "X":
                cross += 1
    if abs(circle - cross) >= 2:
        return 0
    elif circle < cross:
        return 0
    elif isCircleBingo and circle == cross:
        return 0
    elif isCrossBingo and circle == cross + 1:
        return 0
    return answer