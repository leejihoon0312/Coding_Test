import sys

size = int(input())
quickSlot = dict()
for _ in range(size):
    function = list(sys.stdin.readline().strip().split())

    flag = False
    for order in range(len(function)):
        if function[order][0].upper() in quickSlot or function[order][0].lower() in quickSlot:
            continue
        elif function[order][0].upper() not in quickSlot or function[order][0].lower() not in quickSlot:
            quickSlot[function[order][0]] = 1
            function[order] = "[" + function[order][0] + "]" + function[order][1:]
            flag = True
            break

    if flag:
        complete = " ".join(function)
        print(complete)
        continue

    flag = False
    for order in range(len(function)):
        for scan in range(len(function[order])):
            if function[order][scan].upper() in quickSlot or function[order][scan].lower() in quickSlot:
                continue
            elif function[order][scan].upper() not in quickSlot or function[order][scan].lower() not in quickSlot:
                quickSlot[function[order][scan]] = 1
                function[order] = function[order][0:scan] + "[" + function[order][scan] + "]" + function[order][scan+1:]
                flag = True
                break
        if flag:
            break

    complete = " ".join(function)
    print(complete)