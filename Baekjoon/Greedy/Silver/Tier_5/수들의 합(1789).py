
N = int(input())

count = 0
current = N
for i in range(1, N+1):
    if current - i <= i:
        count += 1
        break
    else:
        current -= i
        count += 1
print(count)