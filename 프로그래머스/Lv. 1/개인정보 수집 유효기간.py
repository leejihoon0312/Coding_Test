def solution(today, terms, privacies):
    answer = []

    year, month, day = map(int, today.split("."))
    valid_period = {}

    for term in terms:
        kind, period = term.split()
        valid_period[kind] = int(period)

    for number, privacy in enumerate(privacies, start=1):
        collect, kind = privacy.split()
        collect_year, collect_month, collect_day = map(int, collect.split("."))

        expire_year = collect_year + valid_period[kind] // 12
        expire_month = collect_month + valid_period[kind] % 12
        if expire_month > 12:
            expire_year += expire_month // 12
            expire_month = expire_month % 12

        if collect_day == 1:
            expire_month -= 1
            if expire_month == 0:
                expire_year -= 1
                expire_month = 12
                expire_day = 28
            else:
                expire_day = 28
        else:
            expire_day = collect_day - 1

        if expire_year < year or (expire_year == year and expire_month < month) or (
                expire_year == year and expire_month == month and expire_day < day):
            answer.append(number)

    return answer