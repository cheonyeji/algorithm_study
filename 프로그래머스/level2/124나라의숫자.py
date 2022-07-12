# 2022-07-12
# 프로그래머스 lv2 - 124 나라의 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12899
# 소요 시간 : 16:14 ~ 16:41 (27m)

"""
3으로 나눴을 때의 나머지로 숫자가 결정되며
몫이 3보다 큰 경우 계속하여 나눠주면서 나머지로 숫자를 결정함.
근데 만약 몫이든 숫자든 나눠야하는 숫자가 3의 배수인 경우 규칙에서 어긋남
따라서 3의 배수인 경우 마지막 숫자를 4로 설정해준 뒤 몫-1을 해서 계속하여 연산해주면 ok
"""


def convert(n):
    result = ""
    while n != 0:
        q, r = divmod(n, 3)

        if r == 1:
            result += "1"
            n = q
        elif r == 2:
            result += "2"
            n = q
        else:
            result += "4"
            n = q - 1
    return result[::-1]


def solution(n):
    answer = ""

    if n % 3 == 0:
        answer = convert(n - 1)[:-1] + "4"
    else:
        answer = convert(n)

    return answer
