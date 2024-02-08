def solution(new_id):
    answer = ''
    alphabet = {}
    a = ord("a")
    z = ord("z")
    while a <= z:
        alphabet[chr(a)] = 1
        a = a + 1
    number = [str(i) for i in range(10)]

    # 1
    new_id = new_id.lower()

    # 2
    for id in new_id:
        if id in alphabet or id == "-" or id == "_" or id == "." or id in number:
            answer += id
    # 3
    temp = ""
    for order in range(len(answer) - 1):
        if answer[order] == ".":
            if answer[order + 1] == ".":
                continue
            else:
                temp += answer[order]

        else:
            temp += answer[order]
    temp += answer[-1]
    answer = temp[:]

    # 4
    if answer[-1] == "." and answer[0] == ".":
        answer = answer[1:len(answer) - 1]
    elif answer[-1] == ".":
        answer = answer[:len(answer) - 1]
    elif answer[0] == ".":
        answer = answer[1:]

    # 5
    if len(answer) == 0:
        answer = "a"
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == ".":
        answer = answer[:len(answer) - 1]

        # 7
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    return answer