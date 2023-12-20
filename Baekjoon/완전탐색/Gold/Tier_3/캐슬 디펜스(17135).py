from itertools import combinations
import sys

row, col, D = map(int, sys.stdin.readline().split())

graph = []
enemy_cnt = 0
max_eliminate = 0
for i in range(row):
    ls = list(map(int, sys.stdin.readline().split()))
    for j in range(len(ls)):
        if ls[j] == 1:
            enemy_cnt += 1
    graph.append(ls)
graph.append([0] * col)


def attack(ar, ac):
    for dist in range(1, D+1):
        for c in range(col):
            for r in range(row - 1, -1, -1):
                if copy_graph[r][c] == 1 and (abs(ar - r) + abs(ac - c)) <= dist:
                    return r, c

    return None, None


for location in list(combinations(range(col), 3)):
    copy_graph = [arr[:] for arr in graph]
    archer = []

    eliminate = 0
    disappear = 0
    for i in location:
        archer.append((row, i))
    while eliminate + disappear < enemy_cnt:
        target = set()
        # 궁수가 공격
        for i in range(3):
            archer_r, archer_c = archer[i]
            monster_r, monster_c = attack(archer_r, archer_c)
            if monster_r is not None and monster_c is not None:
                target.add((monster_r, monster_c))

        # 몇마리 제거했는지 체크
        for i in target:
            r, c = i
            copy_graph[r][c] = 0
            eliminate += 1

        # 남은 적들 한칸씩 아래로 이동
        for co in range(col):
            for ro in range(row - 1, -1, -1):
                if ro == row - 1:
                    if copy_graph[ro][co] == 1:
                        copy_graph[ro][co] = 0
                        disappear += 1
                else:
                    if copy_graph[ro][co] == 1:
                        copy_graph[ro][co] = 0
                        copy_graph[ro + 1][co] = 1

        max_eliminate = max(max_eliminate, eliminate)

print(max_eliminate)
