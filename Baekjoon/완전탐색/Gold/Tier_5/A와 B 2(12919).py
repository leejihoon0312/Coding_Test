import sys

sys.setrecursionlimit(10 ** 5)
From = sys.stdin.readline().strip()
To = sys.stdin.readline().strip()
visited = {}


def dfs(start, end):
    if len(start) == len(end) and start != end:
        return

    if len(start) == len(end) and start == end:
        print(1)
        exit(0)

    if end[-1] == "A":
        dfs(start, end[:len(end) - 1])
    if end[0] == "B":
        dfs(start, end[len(end) - 1:0:-1])


dfs(From, To)
print(0)
