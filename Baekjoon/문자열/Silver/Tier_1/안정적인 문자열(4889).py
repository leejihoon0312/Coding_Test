import sys

loop = 1

while True:
    open_stack = []
    close_stack = []
    cnt = 0
    symbol = sys.stdin.readline().strip()
    if "-" in symbol:
        break

    # 바꾸지 않아도 되는 부분
    for sign in range(len(symbol)):
        if symbol[sign] == "{":
            open_stack.append(symbol[sign])

        elif symbol[sign] == "}":
            if len(open_stack) == 0:
                close_stack.append(symbol[sign])
            else:
                open_stack.pop()

    # 1개만 바꿔야 하는 부분
    if len(open_stack) != 0:
        cnt += int(len(open_stack) / 2)

    if len(close_stack) != 0:
        cnt += int(len(close_stack) / 2)

    # 2개 바꿔야 하는 부분
    if len(open_stack) % 2 != 0 and len(close_stack) % 2 != 0:
        cnt += 2
    print(f"{loop}. {cnt}")
    loop += 1
