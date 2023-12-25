import sys

size = int(input())

word = [list(sys.stdin.readline().strip()) for _ in range(size)]

word.sort(key=len)
result = 0
for i in range(size):
    flag = True
    for j in range(i+1, size):

        if len(word[i]) < len(word[j]):
            if word[i] == word[j][0:len(word[i])]:
                flag = False
                break
        if len(word[i]) == len(word[j]) and word[i] == word[j][0:len(word[i])]:
            flag = False
            break

    if flag:
        result += 1

print(result)