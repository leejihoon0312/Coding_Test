def solution(targets):
    answer = 0
    system_loc = []
    targets = sorted(targets, key=lambda x: x[1])
    system_loc.append(targets[0][1] - 0.5)

    for i in range(1, len(targets)):
        if targets[i][0] < system_loc[-1] < targets[i][1]:
            continue
        elif targets[i][0] > system_loc[-1]:
            system_loc.append(targets[i][1] - 0.5)

    answer = len(system_loc)

    return answer