from collections import deque

case = int(input())

result = []


def isPrime(num):
    for i in range(2, int(num ** 1 / 2) + 1):
        if num % i == 0:
            return False
    return True


def bfs(num):
    q = deque()
    q.append((num, 0))
    visited[num] = 1
    global result, flag
    while q:
        cur_num, cnt = q.popleft()

        if cur_num == end:
            flag = False
            result.append(cnt)
            break

        str_num = str(cur_num)

        for i in range(4):
            for j in range(10):

                new_pass = list(str_num)
                new_pass[i] = str(j)
                new_pass = int(''.join(new_pass))

                if new_pass >= 1000 and isPrime(new_pass) and visited[new_pass] == 0:
                    visited[new_pass] = 1
                    q.append((new_pass, cnt + 1))


for _ in range(case):
    start, end = map(int, input().split())
    flag = True
    visited = [0] * 10000

    bfs(start)

    if flag:
        result.append('Impossible')
    visited.clear()

for i in result:
    print(i)
