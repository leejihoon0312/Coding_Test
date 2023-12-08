import sys
sys.setrecursionlimit(10**7)
matrix = []
num = []

for _ in range(5):
    matrix.append(list(sys.stdin.readline().split()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, base_str,count):

    str_num = matrix[r][c]

    base_str += str_num

    if count == 6:
        if int(base_str) not in num:
            num.append(int(base_str))

    else:
        for i in range(4):
            next_r = r + dr[i]
            next_c = c + dc[i]
            if 0 <= next_r < 5 and 0 <= next_c < 5:
                dfs(next_r, next_c, base_str,count+1)





for cur_row in range(5):
    for cur_col in range(5):
        dfs(cur_row, cur_col, "",1)

print(len(num))

