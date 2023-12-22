import sys

word = sys.stdin.readline().strip()
word_dict = dict()
for size in range(1, len(word)+1):

    for i in range(size, len(word)+1):
        sub_str = word[i-size:i]
        if sub_str in word_dict:
            continue
        else:
            word_dict[sub_str] = 1
print(len(word_dict.keys()))