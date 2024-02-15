from collections import defaultdict
from bisect import bisect_left
from itertools import combinations


def solution(info, query):
    answer = []

    infomations = defaultdict(list)
    for supplier in info:
        lang, part, practice, food, score = supplier.split()

        for i in range(5):
            for c in combinations([lang, part, practice, food], i):

                c = list(c)
                t1, t2, t3, t4 = lang, part, practice, food
                if lang not in c:
                    t1 = "-"
                if part not in c:
                    t2 = "-"
                if practice not in c:
                    t3 = "-"
                if food not in c:
                    t4 = "-"
                infomations[(t1, t2, t3, t4)].append(int(score))

    for key in infomations.keys():
        infomations[key].sort()

    for q in query:
        lang, part, practice, food = q.split(" and ")
        food, score = food.split()
        ls = infomations[(lang, part, practice, food)]
        answer.append(len(ls) - bisect_left(ls, int(score)))

    return answer