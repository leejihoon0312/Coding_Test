from collections import deque


def bfs(r, c, num, phone):
    visited = [[False] * 3 for _ in range(4)]
    q = deque()
    visited[r][c] = True
    q.append((r, c, 0))  # 행,열,이동거리

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        cur_r, cur_c, cur_dist = q.popleft()

        if phone[cur_r][cur_c] == num:
            return cur_r, cur_c, cur_dist

        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < 4 and 0 <= next_c < 3 and visited[next_r][next_c] == False:
                visited[next_r][next_c] = True
                q.append((next_r, next_c, cur_dist + 1))


def solution(numbers, hand):
    answer = ''

    phone = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ["*", 0, "#"]
    ]

    cur_left_row = 3
    cur_left_col = 0
    cur_right_row = 3
    cur_right_col = 2

    for number in numbers:
        if number in [1, 4, 7]:
            if number == 1:
                cur_left_row = 0
                cur_left_col = 0
                answer += "L"
            elif number == 4:
                cur_left_row = 1
                cur_left_col = 0
                answer += "L"
            else:
                cur_left_row = 2
                cur_left_col = 0
                answer += "L"
        elif number in [3, 6, 9]:
            if number == 3:
                cur_right_row = 0
                cur_right_col = 2
                answer += "R"
            elif number == 6:
                cur_right_row = 1
                cur_right_col = 2
                answer += "R"
            else:
                cur_right_row = 2
                cur_right_col = 2
                answer += "R"
        else:
            lr, lc, left_dist = bfs(cur_left_row, cur_left_col, number, phone)
            rr, rc, right_dist = bfs(cur_right_row, cur_right_col, number, phone)

            if left_dist < right_dist:
                cur_left_row = lr
                cur_left_col = lc
                answer += "L"
            elif left_dist > right_dist:
                cur_right_row = rr
                cur_right_col = rc
                answer += "R"
            else:
                if hand == "right":
                    cur_right_row = rr
                    cur_right_col = rc
                    answer += "R"
                else:
                    cur_left_row = lr
                    cur_left_col = lc
                    answer += "L"

    return answer