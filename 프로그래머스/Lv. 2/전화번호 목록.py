def solution(phone_book):
    answer = True
    phone_number = {}
    phone_book.sort(key=len)

    for number in phone_book:
        for i in range(1, len(number) + 1):
            if number[:i] in phone_number:
                return False
        phone_number[number] = 1
    return answer