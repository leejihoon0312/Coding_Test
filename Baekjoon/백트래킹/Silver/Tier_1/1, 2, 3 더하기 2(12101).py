N, K = map(int, input().split())
cnt = 1


def backtracking(arr, total):
    global N, K, cnt

    if total == N:
        if cnt == K:
            print("+".join(arr))
            exit(0)
        else:
            cnt += 1
            return

    for num in range(1, 4):
        if total + num <= N:
            arr.append(str(num))
            backtracking(arr[:], total + num)
            arr.pop()


backtracking([], 0)
print(-1)
