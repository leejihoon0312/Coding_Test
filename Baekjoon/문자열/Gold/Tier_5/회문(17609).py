import sys

case = int(input())


def check(word):
    for order in range(int(len(word) / 2)):
        if word[order] != word[-(order + 1)]:
            return False, order

    return True, None


for _ in range(case):
    origin_word = sys.stdin.readline().strip()

    copy_origin_word = origin_word[:]

    result, idx = check(copy_origin_word)

    if result:
        print(0)
        continue
    elif not result:
        flag = True
        for index in [idx, len(origin_word)-idx-1]:
            sec_result, sec_idx = check(origin_word[:index]+origin_word[index+1:])
            if sec_result:
                print(1)
                flag = False
                break
    if flag:
        print(2)
