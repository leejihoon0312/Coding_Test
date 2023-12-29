from collections import deque
import sys

len_S = int(sys.stdin.readline())
result = ""
word = deque()
for _ in range(len_S):
    word.append(sys.stdin.readline().rstrip())
word_cnt = 0


def check(word_ls):
    for order in range(int(len(word_ls) / 2)):
        if word_ls[order] != word_ls[-(order + 1)]:
            if word_ls[order] > word_ls[-(order + 1)]:
                return True, -1
            else:
                return True, 0
    return False, None


while True:

    if word[0] < word[-1]:
        result += word.popleft()

    elif word[0] > word[-1]:
        result += word.pop()


    elif word[0] == word[-1] and len(word) > 1:
        check_result, idx = check(word)
        if check_result:
            if idx == -1:
                result += word.pop()

            else:
                result += word.popleft()
        else:
            result += word.pop()


    elif len(word) == 1:
        result += word.pop()
        break

for i in result:
    print(i, end="")
    word_cnt += 1
    if word_cnt % 80 == 0:
        print()
