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


# 소수 판별 (개선된 알고리즘)
import math


def isPrimeNumber(num):
    # 2부터 num의 제곱근까지의 모든 수를 확인하기
    # 제곱근을 구하는 방법은 math.sqrt() 사용. 반환형은 float
    # 음수의 제곱근을 구하게 되면 error 발생하니 유의
    for i in range(2, int(math.sqrt(num)) + 1):
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
