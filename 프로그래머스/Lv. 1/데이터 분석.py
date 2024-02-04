def solution(data, ext, val_ext, sort_by):
    answer = []

    standard = ["code", "date", "maximum", "remain"]
    idx = standard.index(ext)

    for value in data:
        if value[idx] < val_ext:
            answer.append(value)

    answer = sorted(answer, key=lambda x: x[standard.index(sort_by)])

    return answer