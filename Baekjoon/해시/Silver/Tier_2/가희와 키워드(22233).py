import sys,copy

N, M = map(int, input().split())
keyword = dict()
count = copy.copy(N)
for _ in range(N):
    word = sys.stdin.readline().strip()
    keyword[word] = 1

for loop in range(M):
    ls = list(sys.stdin.readline().strip().split(","))
    for voca in ls:
        if voca in keyword and keyword[voca] != 0:
            keyword[voca] = 0
            count -= 1
    print(count)