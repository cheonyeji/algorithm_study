# 2023-04-12
# 프로그래머스 고득점 kit - 완전탐색
# https://school.programmers.co.kr/learn/courses/30/lessons/84512
# 소요 시간 : 12:16 ~ 12:36 (20m)

from itertools import product


def solution(word):
    letters = ["A", "E", "I", "O", "U"]
    letterDict = []
    for i in range(1, len(letters) + 1):
        for case in list(product(letters, repeat=i)):
            letterDict.append("".join(case))

    letterDict.sort()

    answer = letterDict.index(word) + 1
    return answer
