import sys

case = int(input())
number_dict = dict()


def check(num):
    for idx in range(len(num)):
        if str(number[0:idx + 1]) in number_dict:
            return False
    return True


for _ in range(case):
    number_of_phone = int(input())
    number_ls = []
    flag = True
    for loop in range(number_of_phone):
        number_ls.append(sys.stdin.readline().strip())

    number_ls = sorted(number_ls)

    for number in number_ls:

        if check(number):
            number_dict[number] = 1
        else:
            print("NO")
            flag = False
            break

    if flag:
        print("YES")
    number_dict.clear()
