from collections import defaultdict


def solution(X, Y):
    answer = ""

    x_dict = defaultdict(int)
    y_dict = defaultdict(int)

    for i in X:
        x_dict[i] += 1
    for i in Y:
        y_dict[i] += 1

    for num in range(9, -1, -1):
        if x_dict[str(num)] != 0 and y_dict[str(num)] != 0:
            answer += str(num) * min(x_dict[str(num)], y_dict[str(num)])

    if len(answer) == 0:
        return "-1"
    if answer[0] == "0":
        return "0"
    return answer