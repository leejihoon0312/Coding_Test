import sys
from collections import defaultdict, Counter


def check(word):
    for order in range(int(len(word) / 2)):
        if word[order] != word[-(order + 1)]:
            return False

    return True


origin_word = sys.stdin.readline().strip()

if len(origin_word) == 1 or len(Counter(origin_word).keys()) == 1:
    print(-1)
    exit(0)

if not check(origin_word):
    print(len(origin_word))
    exit(0)
if check(origin_word):
    print(len(origin_word) - 1)
    exit(0)

# word_dict = defaultdict(list)
# maximum = 0
# for idx, value in enumerate(origin_word):
#     word_dict[value].append(idx)
#
#

#
#
# keys = list(word_dict.keys())
#
# for std_idx in range(len(keys)):
#     for comp_idx in range(std_idx, len(keys)):
#
#         if keys[std_idx] == keys[comp_idx] and (abs(word_dict[keys[comp_idx]][-1] - word_dict[keys[std_idx]][0]) + 1) > maximum and word_dict[keys[comp_idx]][-1] != word_dict[keys[std_idx]][0]:
#
#             if not check(origin_word[word_dict[keys[std_idx]][0]: word_dict[keys[comp_idx]][-1] + 1]):
#                 maximum = abs(word_dict[keys[comp_idx]][-1] - word_dict[keys[std_idx]][0]) + 1
#
#         elif keys[std_idx] != keys[comp_idx]:
#             first_first = abs(word_dict[keys[comp_idx]][0] - word_dict[keys[std_idx]][0]) + 1
#             first_end = abs(word_dict[keys[comp_idx]][-1] - word_dict[keys[std_idx]][0]) + 1
#             end_first = abs(word_dict[keys[comp_idx]][0] - word_dict[keys[std_idx]][-1]) + 1
#             end_end = abs(word_dict[keys[comp_idx]][-1] - word_dict[keys[std_idx]][-1]) + 1
#             maximum = max(maximum, first_first, first_end, end_first, end_end)
#
# if maximum == 0:
#     print(-1)
# else:
#     print(maximum)
