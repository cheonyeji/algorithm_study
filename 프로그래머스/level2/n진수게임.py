# 2023-06-15
# 프로그래머스 lv2 - n진수게임
# https://school.programmers.co.kr/learn/courses/30/lessons/17687
# 소요 시간 : 16:25 ~ 17:10 (45m)


def aToF(n):
    if n == 10:
        return "A"
    elif n == 11:
        return "B"
    elif n == 12:
        return "C"
    elif n == 13:
        return "D"
    elif n == 14:
        return "E"
    elif n == 15:
        return "F"
    else:
        return n


def convert(n, base):

    if n == 0:
        return "0"

    num = ""
    while n > 0:
        n, mod = divmod(n, base)
        mod = aToF(mod)
        num += str(mod)
    return num[::-1]


def solution(n, t, m, p):
    answer = ""
    num = 0
    total = ""
    index = 0
    while True:
        cnum = convert(num, int(n))
        total += cnum
        index += len(cnum)
        q, mod = divmod(index, m)  # m명이서 나눠서 말하는 경우
        if q >= t:
            count = 0
            for i in range(len(total)):
                if i % m == (p - 1) and count < t:
                    answer += total[i]
                    count += 1
            break
        num += 1

    return answer
