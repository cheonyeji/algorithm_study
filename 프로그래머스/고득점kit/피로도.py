# 2022-12-16
# 프로그래머스 고득점 kit - 완전탐색
# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 소요 시간 : 16:40 ~ 16:54 (14m)

from itertools import permutations


def solution(k, dungeons):
    origin_k = k
    answer = -1

    idx = []
    for i in range(len(dungeons)):
        idx.append(i)

    all_case = list(permutations(idx, len(dungeons)))

    for case in all_case:
        cnt = 0
        for idx in case:
            min_p, cost_p = dungeons[idx]
            if min_p <= k and cost_p <= k:
                k -= cost_p
                cnt += 1
            else:
                break
        if cnt > answer:
            answer = cnt
        k = origin_k

    return answer
