# 2022-07-22
# 프로그래머스 Lv2 - 소수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 소요시간 : 15:10 ~ 15:25 (15m)

from itertools import permutations

# 소수판별 알고리즘
def checkPrimeNum(num):
    if num == 0 or num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    num_arr = []
    for num in numbers:
        num_arr.append(num)

    every_case = []
    for i in range(1, len(num_arr) + 1):
        case = list(permutations(num_arr, i))
        for arr in case:
            every_case.append(int("".join(arr)))

    every_case = list(set(every_case))

    # print(every_case)

    for case in every_case:
        if checkPrimeNum(case):
            # print(case)
            answer += 1

    return answer
