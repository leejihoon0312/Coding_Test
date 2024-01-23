from bisect import bisect_left, bisect_right

N, C = map(int, input().split())

matrix = [int(input()) for _ in range(N)]

matrix.sort()
start = 1
end = matrix[-1] - matrix[0]
result = 0

if C == 2:
    print(matrix[-1] - matrix[0])
    exit(0)

while start<=end:
    mid = (start+end) // 2
    current = matrix[0]

    iptime = 1
    for i in range(1, N):
        if matrix[i]-current >= mid:
            current = matrix[i]
            iptime += 1

    if iptime>=C:
        start = mid+1
        result = mid
    else:
        end = mid-1


print(result)


