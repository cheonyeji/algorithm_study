# 2022-07-01
# 프로그래머스 lv1 - 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301
# 소요 시간 : 22:04 ~ 22:30 (25m)


def solution(s):
    answer = 0
    words = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    answer = int(s)
    return answer
