def solution(board, moves):
    answer = 0

    stack = []

    row = len(board)
    col = len(board[0])

    for col_num in moves:

        for r in range(row):
            if board[r][col_num - 1] != 0:
                stack.append(board[r][col_num - 1])
                board[r][col_num - 1] = 0
                break
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                for _ in range(2):
                    stack.pop()
                answer += 2

    return answer