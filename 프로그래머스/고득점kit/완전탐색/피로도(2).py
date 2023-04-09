# 2023-04-05
# 프로그래머스 고득점 kit - 완전탐색
# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 소요 시간 : 19:10

from itertools import permutations


def solution(k, dungeons):
    answer = -1

    originK = k

    for cases in list(permutations(dungeons, len(dungeons))):
        count = 0
        for dungeon in cases:
            if k >= dungeon[0]:
                count += 1
                k -= dungeon[1]
        k = originK
        answer = max(count, answer)
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
