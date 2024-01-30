from collections import defaultdict


def solution(friends, gifts):
    answer = 0
    give = defaultdict(int)
    in_present = defaultdict(int)
    out_present = defaultdict(int)
    result = defaultdict(int)
    for gift in gifts:
        from_f, to_f = gift.split()
        give[(from_f, to_f)] += 1
        in_present[to_f] += 1
        out_present[from_f] += 1

    for f1_num in range(len(friends)):
        for f2_num in range(f1_num + 1, len(friends)):
            # 주고받은 기록이 없거나 주고 받은게 같다면
            if ((friends[f1_num], friends[f2_num]) not in give and (friends[f2_num], friends[f1_num]) not in give) or (
                    give[(friends[f1_num], friends[f2_num])] == give[(friends[f2_num], friends[f1_num])]):
                # 친구 1의 선물지수가 더 낮을 때
                if out_present[friends[f1_num]] - in_present[friends[f1_num]] < out_present[friends[f2_num]] - \
                        in_present[friends[f2_num]]:
                    # 친구 2가 선물을 받아야함
                    result[friends[f2_num]] += 1
                # 친구 2의 선물지수가 더 낮을 때
                elif out_present[friends[f1_num]] - in_present[friends[f1_num]] > out_present[friends[f2_num]] - \
                        in_present[friends[f2_num]]:
                    # 친구 1이 선물을 받아야함
                    result[friends[f1_num]] += 1
            # 기록이 있을때
            else:
                if give[(friends[f1_num], friends[f2_num])] > give[(friends[f2_num], friends[f1_num])]:
                    # 친구 1이 선물을 받아야함
                    result[friends[f1_num]] += 1

                elif give[(friends[f1_num], friends[f2_num])] < give[(friends[f2_num], friends[f1_num])]:
                    # 친구 2가 선물을 받아야함
                    result[friends[f2_num]] += 1

    if len(result.values()) > 0:
        answer = max(result.values())

    return answer