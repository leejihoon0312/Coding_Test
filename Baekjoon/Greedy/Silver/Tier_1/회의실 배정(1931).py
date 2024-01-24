
N = int(input())

room = [list(map(int, input().split())) for _ in range(N)]

room = sorted(room, key=lambda x:(x[1],x[0]))
meeting_end_time = 0

count = 0
for start, end in room:
    if meeting_end_time > start:
        continue
    else:
        meeting_end_time = end
        count += 1

print(count)
