size = int(input())

num_list = list(map(int, input().split(" ")))

maximum = num_list[0]
sum = 0
for i in range(size):
    sum += num_list[i]
    maximum = max(maximum, sum)
    if sum <= 0:
        sum = 0

print(maximum)
