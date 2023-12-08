dwarf = []
for _ in range(9):
    dwarf.append(int(input()))


def find_two_dwarf(dwarf):
    height = sum(dwarf)
    for i in range(9):
        for j in range(i+1, 9):
            if height-dwarf[i]-dwarf[j] == 100:
                first, second = dwarf[i],dwarf[j]
                dwarf.remove(first)
                dwarf.remove(second)
                return dwarf


dwarf = find_two_dwarf(dwarf)
dwarf.sort()
for i in dwarf:
    print(i)
