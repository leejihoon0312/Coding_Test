def solution(n, lost, reserve):
    answer = 0

    can_reserve = set(reserve) - set(lost)
    have_nothing = set(lost) - set(reserve)

    for reserve_student in can_reserve:
        if reserve_student - 1 in have_nothing:
            have_nothing.remove(reserve_student - 1)
        elif reserve_student + 1 in have_nothing:
            have_nothing.remove(reserve_student + 1)

    answer = n - len(have_nothing)

    return answer