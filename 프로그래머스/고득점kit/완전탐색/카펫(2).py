# 2023-04-05
# 프로그래머스 고득점 kit - 완전탐색
# https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 소요 시간 : 18:28 ~ 18:48 (15m)
import math


def getDivisor(num):
    divisor = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisor.append([i, num // i])

    return divisor


def solution(brown, yellow):
    answer = []

    divisor = getDivisor(yellow)

    for case in divisor:
        num1, num2 = case
        if (2 * (num1 + num2) + 4) == brown:
            if num1 >= num2:
                answer.append(num1 + 2)
                answer.append(num2 + 2)
            else:
                answer.append(num2 + 2)
                answer.append(num1 + 2)
    return answer
