T = int(input())

for test_case in range(1, T + 1):
    cnt = int(input())
    price = list(map(int, input().split()))

    use_money = 0
    stock = 0
    earn_money = 0

    max_price = max(price)
    for idx, value in enumerate(price):
        if value == max_price:
            earn_money += (value*stock) - use_money
            use_money = 0
            stock = 0
            if idx+1 != len(price):
                max_price = max(price[idx+1:])

        else:
            use_money += value
            stock += 1

    print(f"#{test_case} {earn_money}")