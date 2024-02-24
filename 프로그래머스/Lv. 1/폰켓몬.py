from collections import Counter
def solution(nums):
    answer = 0
    if len(Counter(nums)) < len(nums)//2:
        answer = len(Counter(nums))
    else:
        answer = len(nums)//2
    return answer