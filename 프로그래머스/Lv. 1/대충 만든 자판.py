from collections import defaultdict


def solution(keymap, targets):
    answer = []

    alphabet = defaultdict(int)

    for key in keymap:
        for idx, word in enumerate(key, start=1):
            if alphabet[word] == 0:
                alphabet[word] = idx
            else:
                alphabet[word] = idx if alphabet[word] > idx else alphabet[word]

    for target in targets:
        value = 0
        flag = True
        for word in target:
            if word in alphabet:
                value += alphabet[word]
            else:
                flag = False
                answer.append(-1)
                break
        if flag:
            answer.append(value)
    return answer