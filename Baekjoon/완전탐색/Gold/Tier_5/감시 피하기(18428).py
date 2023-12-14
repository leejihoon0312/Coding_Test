from itertools import combinations
import sys, copy
N = row = col = int(input())
teacher = []
student = []
graph = []
obj = []

for i in range(row):
    ls = list(sys.stdin.readline().split())
    for j in range(len(ls)):
        if ls[j] == "T":
            teacher.append((i, j))
        if ls[j] == "S":
            student.append((i, j))
        if ls[j] == "X":
            obj.append((i, j))
    graph.append(ls)


def check():
    for t_r, t_c in teacher:

        for left in range(1, N+1):
            if 0<=t_c-left:
                if copy_graph[t_r][t_c-left] == "S":
                    return False
                if copy_graph[t_r][t_c - left] == "O":
                    break
        for right in range(1, N+1):
            if t_c+right<col:
                if copy_graph[t_r][t_c+right] == "S":
                    return False
                if copy_graph[t_r][t_c+right] == "O":
                    break
        for top in range(1, N+1):
            if 0<=t_r-top:
                if copy_graph[t_r-top][t_c] == "S":
                    return False
                if copy_graph[t_r-top][t_c] == "O":
                    break
        for bottom in range(1, N+1):
            if t_r+bottom<row:
                if copy_graph[t_r+bottom][t_c] == "S":
                    return False
                if copy_graph[t_r+bottom][t_c] == "O":
                    break
    return True



# 빈 공간중 랜덤하게 3곳 위치지정
obj_list = list(combinations(obj,3))

for location in obj_list:
    copy_graph = copy.deepcopy(graph)

    # 빈 공간에 장애물 설치
    for i in range(3):
        r, c = location[i]
        copy_graph[r][c] = "O"

    # 선생님들 위치에서 상하좌우 체크
    if check():
        print('YES')
        exit(0)

print("NO")



