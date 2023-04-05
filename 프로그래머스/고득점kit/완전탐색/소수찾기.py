# 2023-04-05
# 프로그래머스 고득점 kit - 완전탐색
# https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 소요 시간 : 17:19 ~ 18:25 (40m)

from itertools import permutations
import math

# 소수 판별 알고리즘
def isPrimeNumber(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    numberArr = list(numbers)
    cases = []
    for i in range(1, len(numberArr) + 1):
        for num in list(permutations(numberArr, i)):
            cases.append(int("".join(num)))
    cases = list(set(cases))

    for case in cases:
        if isPrimeNumber(case):
            answer += 1
    return answer


print(solution("011"))
