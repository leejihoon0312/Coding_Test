import sys

word, length = map(int, sys.stdin.readline().split())

words = dict()
for _ in range(word):
    Str = sys.stdin.readline().strip()
    if len(Str) < length:
        continue
    if Str in words:
        words[Str][0] += 1
    else:
        words[Str] = [1, len(Str), Str]

for i in sorted(words.values(), key=lambda x:(-x[0], -x[1], x[2])):
    print(i[2])
