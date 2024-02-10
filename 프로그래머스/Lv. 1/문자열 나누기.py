def solution(s):
    answer = 0

    flag_word = s[0]
    flag_word_cnt = 1
    not_flag_word_cnt = 0

    for num in range(1, len(s)):

        if flag_word == "":
            flag_word = s[num]
            flag_word_cnt = 1
            not_flag_word_cnt = 0
            continue

        if s[num] == flag_word:
            flag_word_cnt += 1

        else:
            not_flag_word_cnt += 1

        if not_flag_word_cnt == flag_word_cnt:
            flag_word = ""
            flag_word_cnt = 0
            not_flag_word_cnt = 0
            answer += 1

    if flag_word_cnt != not_flag_word_cnt:
        answer += 1

    return answer