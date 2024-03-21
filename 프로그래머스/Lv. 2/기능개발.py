from collections import deque


def solution(progresses, speeds):
    answer = []
    q = deque(progresses)
    sq = deque(speeds)

    while q:

        for idx, _ in enumerate(q):
            q[idx] = q[idx] + sq[idx]

        cnt = 0

        while q:
            if q[0] >= 100:
                q.popleft()
                sq.popleft()
                cnt += 1
            else:
                break

        if cnt > 0:
            answer.append(cnt)

    return answer