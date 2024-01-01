import sys

test_case = int(input())




def backtracking(position, player_num, overall):
    global max_num

    if len(position) == 11:
        max_num = max(max_num, overall)
        return

    for position_num in range(11):
        if graph[player_num][position_num] != 0 and position_num not in position:
            position.append(position_num)
            backtracking(position[:], player_num + 1, overall + graph[player_num][position_num])
            position.pop()


for _ in range(test_case):
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(11)]
    max_num = 0
    backtracking([], 0, 0)
    print(max_num)
