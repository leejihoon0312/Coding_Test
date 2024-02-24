from itertools import product


def solution(users, emoticons):
    discount = [0.1, 0.2, 0.3, 0.4]

    subscriber = 0
    sale = 0

    for rate in set(product(discount, repeat=len(emoticons))):
        temp_subscriber = 0
        temp_sale = 0
        for user in users:
            purchase = 0

            for i in range(len(emoticons)):
                if user[0] <= rate[i] * 100:
                    purchase += emoticons[i] * (1 - rate[i])
            if purchase >= user[1]:
                purchase = 0
                temp_subscriber += 1
            elif purchase < user[1]:
                temp_sale += purchase
        if temp_subscriber > subscriber:
            subscriber = temp_subscriber
            sale = temp_sale
        elif temp_subscriber == subscriber:
            if temp_sale > sale:
                sale = temp_sale

    return [subscriber, int(sale)]