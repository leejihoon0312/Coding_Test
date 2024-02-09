def solution(s, skip, index):
    answer = list(s[:])

    for i in range(len(s)):

        count = 0
        while count < index:
            if not chr(ord(answer[i]) + 1).isalpha():
                if "a" in skip:
                    answer[i] = "a"
                else:
                    answer[i] = "a"
                    count += 1

            else:
                if chr(ord(answer[i]) + 1) in skip:
                    answer[i] = chr(ord(answer[i]) + 1)
                else:
                    answer[i] = chr(ord(answer[i]) + 1)
                    count += 1

    return "".join(answer)