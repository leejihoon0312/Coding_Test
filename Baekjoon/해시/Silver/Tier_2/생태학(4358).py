import sys
from collections import Counter

wood_list = []
while True:
    wood_name = sys.stdin.readline().rstrip()
    if wood_name == '':
        break

    wood_list.append(wood_name)

wood_dict = dict(Counter(wood_list))

wood_dict = dict(sorted(wood_dict.items(), key=lambda x:x[0]))

total = sum(wood_dict.values())

for name, num in wood_dict.items():
    percent = num/total*100
    print(f"{name} {percent:.4f}")