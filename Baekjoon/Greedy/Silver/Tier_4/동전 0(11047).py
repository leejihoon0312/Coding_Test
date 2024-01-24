
N, K=map(int, input().split())

coin = [int(input()) for _ in range(N)]

coin.reverse()


number_of_coin = 0
money = K

for i in coin:
    number_of_coin += money // i
    money = money%i

print(number_of_coin)

