import sys

non_hear, non_see = map(int, input().split())

hear = set()
see = set()

for _ in range(non_hear):
    hear.add(sys.stdin.readline().strip())

for _ in range(non_see):
    see.add(sys.stdin.readline().strip())

non_hear_and_non_see = hear & see

ls = sorted(non_hear_and_non_see)

print(len(ls))
for i in ls:
    print(i)