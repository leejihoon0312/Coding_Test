from collections import Counter
import sys

card_num = int(input())

hold_card_dict = Counter(list(map(int, sys.stdin.readline().split())))

check_num = int(input())

for i in list(map(int, sys.stdin.readline().split())):
    print(hold_card_dict[i], end=" ")
