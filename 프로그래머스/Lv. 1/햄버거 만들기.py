def solution(ingredient):
    answer = 0
    stack = []

    for food in ingredient:
        stack.append(food)

        if len(stack) >= 4:
            if stack[len(stack) - 4:len(stack)] == [1, 2, 3, 1]:
                for _ in range(4):
                    stack.pop()
                answer += 1

    return answer