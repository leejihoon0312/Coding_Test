import sys

R, C = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

max_depth = 0


def backtracking(cur_row, cur_col, alpha_set, depth):
    global max_depth

    if depth > max_depth:
        max_depth = depth

    for i in range(4):
        next_r = cur_row + dr[i]
        next_c = cur_col + dc[i]
        if 0 <= next_r < R and 0 <= next_c < C and graph[next_r][next_c] not in alpha_set:
            alpha_set.add(graph[next_r][next_c])
            backtracking(next_r, next_c, alpha_set, depth + 1)
            alpha_set.remove(graph[next_r][next_c])


alphabet_set = set()
alphabet_set.add(graph[0][0])
backtracking(0, 0, alphabet_set, 1)
print(max_depth)
