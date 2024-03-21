def solution(s):
    stack = []

    for symbol in s:
        if symbol == "(":
            stack.append("(")
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True

    return False
