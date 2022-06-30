# 2022-06-30
# 프로그래머스 lv1 - 3진법 뒤집기
# https://programmers.co.kr/learn/courses/30/lessons/68935
# 소요 시간 : 18:24 ~ 18:35 (10m)

# 10진법 -> 3진법인데 거꾸로 들어감
def convert10to3(n):
    result = ""
    while True:
        result += str(int(n % 3))
        if int(n / 3) == 0:
            break
        n = int(n / 3)
    return result


def convert3to10(str_n):
    result = 0
    for i in range(len(str_n)):
        result += 3 ** (len(str_n) - 1 - i) * int(str_n[i])
    return result


def solution(n):
    answer = convert10to3(n)
    answer = convert3to10(answer)
    return answer
