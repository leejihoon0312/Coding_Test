num = int(input())


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 1 / 2) + 1):
        if n % i == 0:
            return False
    return True


def isPalin(n):
    str_num = str(n)
    str_num = list(str_num)
    str_num.reverse()
    if int("".join(str_num)) == n:
        return True
    return False


while True:
    if isPalin(num) and isPrime(num):
        print(num)
        exit(0)
    num += 1
