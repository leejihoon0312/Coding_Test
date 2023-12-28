import sys

word = list(sys.stdin.readline().strip())

stack = []

while word:

    stack.append(word.pop())

    if len(stack)>=4:
        if "".join(stack[-1: -5:-1]) == "PPAP":
            word.append("P")
            for _ in range(4):
                stack.pop()

if "".join(stack) == "P":
    print("PPAP")
else:
    print("NP")

