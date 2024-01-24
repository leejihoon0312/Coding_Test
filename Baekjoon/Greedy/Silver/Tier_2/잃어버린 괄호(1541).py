import sys,re

string = sys.stdin.readline().strip()

string = re.split('([-|+])',string)
result = ""

isOpen = False

for word in string:
    if word == "-":
        if not isOpen:
            result = result + word + "("
            isOpen = True
        else:
            result = result + ")" +word + "("
    elif word == "+":
        result += word

    else:
        result += str(int(word))

if isOpen:
    result += ")"

print(eval(result))
