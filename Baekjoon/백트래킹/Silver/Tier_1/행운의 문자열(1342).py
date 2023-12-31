import sys
from collections import Counter

word = sys.stdin.readline().strip()
word_dict = Counter(word)

result = 0
def backtracking(array):

    global result

    if len(array) == len(word):
        result += 1
        return

    for key in word_dict.keys():
        if word_dict[key] > 0 and array[-1] != key:
            array.append(key)
            word_dict[key] -= 1
            backtracking(array[:])
            array.pop()
            word_dict[key] += 1

for start_key in word_dict.keys():
    arr = [start_key]
    word_dict[start_key] -= 1
    backtracking(arr)
    word_dict[start_key] += 1

print(result)