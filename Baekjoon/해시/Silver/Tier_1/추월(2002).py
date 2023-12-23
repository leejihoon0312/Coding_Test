import sys
from collections import deque
number_of_car = int(input())
enter = []
q = deque()
for _ in range(number_of_car):
    enter.append(sys.stdin.readline().strip())

for _ in range(number_of_car):
    q.append(sys.stdin.readline().strip())

idx = 0
result = 0
while q:
    car_name = q.popleft()

    if enter[idx] == car_name:
        idx += 1
    else:

        del enter[enter.index(car_name)]
        result += 1

print(result)