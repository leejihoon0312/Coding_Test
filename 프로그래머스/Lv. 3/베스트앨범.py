from collections import defaultdict
import heapq


def solution(genres, plays):
    answer = []

    genre = defaultdict(list)

    for unique_num, play in enumerate(plays):
        genre[genres[unique_num]].append((play, unique_num))

    pq = []

    for key in genre.keys():
        genre[key].sort(key=lambda x: (-x[0], x[1]))
        if len(genre[key]) >= 2:
            total_play = 0
            for ls in genre[key]:
                total_play += ls[0]
            heapq.heappush(pq, (-total_play, [genre[key][0][1], genre[key][1][1]]))
        else:
            heapq.heappush(pq, (-genre[key][0][0], [genre[key][0][1]]))

    while pq:
        _, ls = heapq.heappop(pq)
        answer += ls

    return answer