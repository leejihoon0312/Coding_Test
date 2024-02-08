from collections import defaultdict


def solution(survey, choices):
    answer = ''

    mbti_score = defaultdict(int)
    compare = ["RT", "CF", "JM", "AN"]

    for order in range(len(survey)):
        if choices[order] > 4:
            mbti_score[survey[order][1]] += (choices[order] - 4)
        elif choices[order] < 4:
            mbti_score[survey[order][0]] += (4 - choices[order])

    for i in range(4):
        if mbti_score[compare[i][0]] >= mbti_score[compare[i][1]]:
            answer += compare[i][0]
        elif mbti_score[compare[i][0]] < mbti_score[compare[i][1]]:
            answer += compare[i][1]

    return answer

