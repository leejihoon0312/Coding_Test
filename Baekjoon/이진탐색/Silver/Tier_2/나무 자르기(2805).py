import sys

N, M = map(int, input().split())

trees = list(map(int, sys.stdin.readline().split()))

start = 1
end  = max(trees)
mid = min(trees)

def bisect(target, start, end, mid):
    while start <= end:

        cutting_tree = 0
        for tree in trees:
            if tree>mid:
                cutting_tree = cutting_tree + tree-mid

        if cutting_tree == target:
            return mid
        elif cutting_tree > target:
            start = mid + 1

        else:
            end = mid - 1

        mid = (start+end) // 2

    return end

print(bisect(M, start, end, mid))