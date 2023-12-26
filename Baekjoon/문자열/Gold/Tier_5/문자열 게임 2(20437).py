import sys
from collections import defaultdict

times = int(input())

for _ in range(times):
    word = sys.stdin.readline().strip()
    K = int(input())
    word_dict = defaultdict(list)
    minimum = 100000
    maximum = 0
    for idx, value in enumerate(word):
        word_dict[value].append(idx)

    delete_key = []

    for key in word_dict.keys():
        if len(word_dict[key]) < K:
            delete_key.append(key)

    for delete in delete_key:
        del word_dict[delete]

    for value_ls in word_dict.values():
        for index in range(K, len(value_ls)+1):
            minimum = min(minimum, value_ls[index-1] - value_ls[index-K] + 1)
            maximum = max(maximum, value_ls[index - 1] - value_ls[index - K] + 1)
    if minimum != 100000 and maximum != 0:
        print(f"{minimum} {maximum}")
    else:
        print(-1)