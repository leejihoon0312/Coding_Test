import math

N = int(input())

prime = [2, 3, 5, 7]

if N == 1:
    for number in prime:
        print(number)


def isPrime(number):
    for div in range(2, int(math.sqrt(number)) + 1):
        if number % div == 0:
            return False

    return True


def backtracking(arr):
    if len(arr) > 1:

        if not isPrime(int("".join(arr))):
            return
        else:
            if len(arr) == N:
                print(int("".join(arr)))
                return

    for num in range(1, 10, 2):
        arr.append(str(num))
        backtracking(arr[:])
        arr.pop()


for number in prime:
    backtracking([str(number)])
