from collections import Counter


def solution(X, Y):
    answer = ""

    common = dict(Counter(X) & Counter(Y))

    common = list(sorted(common.items(), key=lambda x: x[0], reverse=True))

    for value, loop in common:
        answer += (value * loop)

    if len(answer) == 0:
        return "-1"

    if answer[0] == "0":
        return "0"

    return answer