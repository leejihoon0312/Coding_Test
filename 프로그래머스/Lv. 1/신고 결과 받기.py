from collections import defaultdict


def solution(id_list, report, k):
    answer = []

    # 나를 누가 신고했는지에 대한 목록
    report_Stack = defaultdict(set)

    # 받은 메일 수
    mail = defaultdict(int)

    for people in report:
        from_p, to_p = people.split()
        report_Stack[to_p].add(from_p)

        # 10^6
    for key in report_Stack.keys():
        if len(report_Stack[key]) >= k:
            for reporter in report_Stack[key]:
                mail[reporter] += 1

    for character_id in id_list:
        answer.append(mail[character_id])

    return answer