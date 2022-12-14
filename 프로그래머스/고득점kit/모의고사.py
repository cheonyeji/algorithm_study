# 2022-12-14
# 프로그래머스 고득점 kit - 완전탐색
# https://school.programmers.co.kr/learn/courses/30/lessons/42840
# 소요 시간 : 17:30 ~ 17:40 (10m)

"""
최대한 코드를 간결하게 적어보려고 노력한 문제
"""


def solution(answers):
    answer = []

    s = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    hit = [0, 0, 0]
    for i in range(len(answers)):
        for j in range(len(s)):
            if answers[i] == s[j][i % len(s[j])]:
                hit[j] += 1

    max_hit = max(hit)

    for i in range(len(hit)):
        if max_hit == hit[i]:
            answer.append(i + 1)

    return answer
