
infinite = dict()

N, P, Q = map(int, input().split())

def TopDown(num):

    if num == 0:
        return 1
    if num in infinite:
        return infinite[num]

    infinite[num] = TopDown(int(num / P)) + TopDown(int(num / Q))
    return infinite[num]

print(TopDown(N))