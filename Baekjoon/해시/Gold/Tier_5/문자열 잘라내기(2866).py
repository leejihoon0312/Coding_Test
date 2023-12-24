import sys

row, col = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().strip()) for _ in range(row)]

word_dict = dict()
arr = []
count = 0

for c in range(col):
    temp = ""
    for r in range(1, row):
        temp += graph[r][c]
    arr.append(temp)

graph.clear()

for i in range(row-1):
    for j in range(len(arr)):
        if arr[j][i:row-1] in word_dict:
            print(count)
            exit(0)
        elif arr[j][i:row-1] not in word_dict:
            word_dict[arr[j][i:row-1]] = 1
    count += 1
    word_dict.clear()
print(count)
