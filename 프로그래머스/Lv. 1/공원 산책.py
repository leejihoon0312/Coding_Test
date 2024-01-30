def solution(park, routes):
    row = len(park)
    col = len(park[0])

    # 북, 남, 서, 동
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    directions = ["N", "S", "W", "E"]

    start_row = 0
    start_col = 0
    for r in range(row):
        for c in range(col):
            if park[r][c] == "S":
                start_row = r
                start_col = c
                break

    cur_row = start_row
    cur_col = start_col
    for route in routes:
        direction, num = route.split()
        flag = True
        direct_idx = directions.index(direction)

        temp_row = cur_row
        temp_col = cur_col
        for loop in range(1, int(num) + 1):
            next_row = temp_row + dr[direct_idx]
            next_col = temp_col + dc[direct_idx]

            if 0 <= next_row < row and 0 <= next_col < col and park[next_row][next_col] != "X":
                temp_row = next_row
                temp_col = next_col
            else:
                flag = False
                break

        if flag:
            cur_row = temp_row
            cur_col = temp_col

    answer = [cur_row, cur_col]
    return answer