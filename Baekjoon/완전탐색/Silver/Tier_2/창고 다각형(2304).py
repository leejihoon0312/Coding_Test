

pole = int(input())

arr = []
max_h = 0
max_x = 0
dic_x = {}
for _ in range(pole):
    x, y = map(int, input().split())
    if y>max_h:
        max_h = y
        max_x = x
    arr.append((x, y))
    dic_x[x] = y

arr.sort()

cur_h = arr[0][1]
size = 0
for i in range(arr[0][0], max_x):
    if i not in dic_x:
        size += cur_h
    if i in dic_x:
        if dic_x[i] > cur_h:
            cur_h = dic_x[i]
            size += cur_h
        else:
            size += cur_h



cur_h = arr[-1][1]
for i in range(arr[-1][0], max_x, -1):
    if i not in dic_x:
        size += cur_h
    if i in dic_x:
        if dic_x[i] > cur_h:
            cur_h = dic_x[i]
            size += cur_h
        else:
            size += cur_h



print(size + dic_x[max_x])