from collections import defaultdict


def solution(clothes):
    answer = 1
    category = defaultdict(list)
    for cloth in clothes:
        category[cloth[1]].append(cloth[0])

    for key in category.keys():
        answer *= len(category[key]) + 1

    return answer - 1