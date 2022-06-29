# 2022-06-29
# 프로그래머스 lv1 - 소수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42746
# 소요 시간 : 19:45 ~ 19:55 (10m)

from itertools import combinations


def check(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    datas = combinations(nums, 3)

    for data in datas:
        # 소수 기준 : 자기 자신 외에 어떤 수로 나누어 떨어지면X
        if check(sum(data)):
            answer += 1
            print(data)

    return answer
