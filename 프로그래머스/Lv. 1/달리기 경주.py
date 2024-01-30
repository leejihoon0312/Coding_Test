def solution(players, callings):
    answer = []

    # 위치로 이름찾기
    order = {}

    # 이름으로 위치찾기
    name = {}

    count = 1
    for player in players:
        order[count] = player
        name[player] = count
        count += 1

    for called_player in callings:
        called_player_idx = name[called_player]

        pervious_player = order[called_player_idx - 1]

        pervious_player_idx = name[pervious_player]

        name[pervious_player] = pervious_player_idx + 1
        name[called_player] = called_player_idx - 1

        order[pervious_player_idx + 1] = pervious_player
        order[called_player_idx - 1] = called_player

    for i in range(1, len(players) + 1):
        answer.append(order[i])

    return answer