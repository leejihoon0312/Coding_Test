to_know = int(input())



def constructor(num):
    for i in range(1, num):
        str_num = str(i)
        plus = 0
        for j in range(len(str_num)):
            plus += int(str_num[j])
        result = plus + i
        if result == num:
            return i
    return 0


print(constructor(to_know))
