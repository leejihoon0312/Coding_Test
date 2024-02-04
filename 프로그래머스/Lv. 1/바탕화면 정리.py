def solution(wallpaper):
    answer = []
    row = len(wallpaper)
    col = len(wallpaper[0])

    for r in range(row):
        if "#" in wallpaper[r]:
            answer.append(r)
            break

    for c in range(col):
        flag = False
        for r in range(row):
            if wallpaper[r][c] == "#":
                answer.append(c)
                flag = True
                break
        if flag:
            break

    for r in range(row - 1, -1, -1):
        if "#" in wallpaper[r]:
            answer.append(r + 1)
            break

    for c in range(col - 1, -1, -1):
        flag = False
        for r in range(row):
            if wallpaper[r][c] == "#":
                answer.append(c + 1)
                flag = True
                break
        if flag:
            break

    return answer