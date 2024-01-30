def solution(bandage, health, attacks):
    answer = 0
    skill_time, sec_heal, add_heal = bandage[0], bandage[1], bandage[2]
    cur_health = health
    last_Att_time = attacks[-1][0]
    Att_time = {}
    for attack in attacks:
        Att_time[attack[0]] = attack[1]

    cur_skill_time = 0
    for time in range(1, last_Att_time + 1):

        if time in Att_time:
            cur_skill_time = 0
            cur_health -= Att_time[time]
            if cur_health <= 0:
                return -1

        elif time not in Att_time:
            cur_skill_time += 1
            if cur_skill_time == skill_time:
                cur_skill_time = 0
                cur_health += add_heal + sec_heal
            else:
                cur_health += sec_heal

            if cur_health > health:
                cur_health = health

    answer = cur_health
    return answer