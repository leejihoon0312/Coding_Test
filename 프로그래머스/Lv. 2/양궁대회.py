result = [0, []]


def backtracking(arr, arrow_cnt, n, info):
    global result
    if len(arr) > 11 or arrow_cnt > n:
        return

    if arrow_cnt == n:

        apeach = 0
        lion = 0
        arr = arr + [0] * (11 - len(arr))

        for i in range(len(arr)):
            if info[i] == arr[i] == 0:
                continue
            if info[i] >= arr[i]:
                apeach += 10 - i
            else:
                lion += 10 - i
        if lion > apeach and result[0] <= lion - apeach:
            if result[0] < lion - apeach:
                result.clear()
                result.append(lion - apeach)
                result.append(arr)
            elif result[0] == lion - apeach:
                for j in range(10, -1, -1):
                    if result[1][j] < arr[j]:
                        result.clear()
                        result.append(lion - apeach)
                        result.append(arr)
                        break
                    elif result[1][j] > arr[j]:
                        break
            return

    for i in range(11):
        arr.append(i)
        backtracking(arr, arrow_cnt + i, n, info)
        arr.pop()


def solution(n, info):
    answer = []
    global result
    # 우승못하는 경우
    if all(info[:n]):
        return [-1]

    backtracking([], 0, n, info)

    answer = result[1]

    return answer