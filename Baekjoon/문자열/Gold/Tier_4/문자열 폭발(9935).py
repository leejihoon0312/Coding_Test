
import sys

word = list(sys.stdin.readline().strip())
boom = list(sys.stdin.readline().strip())
stack = []
while word:
    stack.append(word.pop())

    if len(stack) >= len(boom):
        if stack[-1:-len(boom)-1:-1] == boom[:]:
            for i in range(len(boom)):
                stack.pop()


if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack[::-1]))