import sys

pokemon_num, quiz = map(int, input().split())
pokemon_dict = dict()
result = []
for i in range(1, pokemon_num+1):
    name = sys.stdin.readline().strip()
    pokemon_dict[name.lower()] = i
    pokemon_dict[str(i)] = name

for _ in range(quiz):
    problem = sys.stdin.readline().strip().lower()
    result.append(pokemon_dict[problem])

for i in result:
    print(i)

