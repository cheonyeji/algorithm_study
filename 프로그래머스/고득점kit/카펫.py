# 2022-12-16
# 프로그래머스 고득점 kit - 완전탐색
# https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 소요 시간 : 16:20 ~ 16:35 (15m)


def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(3, total):
        if total % i == 0:
            if (i - 2) * ((total // i) - 2) == yellow:
                answer = [total // i, i]
                break
    return answer
