from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque(priorities)
    check_max = sorted(priorities)

    while q:

        if q[0] == check_max[-1]:
            if location == 0:
                return answer + 1
            else:
                answer += 1
                check_max.pop()
                q.popleft()
                location -= 1

        elif q[0] != check_max[-1]:
            if location == 0:
                q.append(q.popleft())
                location = len(q) - 1
            else:
                q.append(q.popleft())
                location -= 1