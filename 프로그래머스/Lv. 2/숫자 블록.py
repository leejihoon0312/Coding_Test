import math


def getPrime(number):
    if number == 1:
        return 0
    divide = [1]
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            divide.append(i)
            if number // i <= 1e7:
                divide.append(number // i)

    return max(divide)


def solution(begin, end):
    answer = []

    for num in range(begin, end + 1):
        answer.append(getPrime(num))

    return answer