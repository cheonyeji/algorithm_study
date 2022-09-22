# 2022-09-22
# 2022 KAKAO BLIND RECRUITMENT 기출 - 양궁대회 (프로그래머스 lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/92342
# 소요 시간 : 3hours, 0.5솔... 해설 참고함

from collections import deque


def shoot(n, info):
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    result = []  # 가능한 시나리오 모두 저장
    max_gap = 0  # 최대 점수차

    while q:
        score, lion = q.popleft()

        # 화살 다 쐈으니 점수 계산
        if sum(lion) == n:
            score_ap, score_l = 0, 0
            for i in range(11):
                if not (info[i] == 0 and lion[i] == 0):
                    if info[i] >= lion[i]:
                        score_ap += 10 - i
                    else:
                        score_l += 10 - i

            if score_ap < score_l:
                gap = score_l - score_ap
                if max_gap > gap:
                    continue
                if max_gap < gap:
                    max_gap = gap
                    result.clear()
                result.append(lion)
        # 화살을 n발보다 더 쏜 경우
        elif sum(lion) > n:
            continue

        # 마지막 과녁까지 간 경우, 화살 마지막 과녁에 다 쏘기
        elif score == 10:
            tmp = lion.copy()
            tmp[score] = n - sum(tmp)
            q.append((-1, tmp))

        # 슛슛슛
        else:
            # 어피치보다 1발 더
            shoot_lion = lion.copy()
            shoot_lion[score] = info[score] + 1
            q.append((score + 1, shoot_lion))
            # 해당 점수 포기, 패스
            giveup_lion = lion.copy()
            giveup_lion[score] = 0
            q.append((score + 1, giveup_lion))

    return result


def solution(n, info):
    answer = []

    all_cases = shoot(n, info)

    if len(all_cases) == 0:
        answer.append(-1)
    elif len(all_cases) == 1:
        answer = all_cases[0]
    else:
        answer = all_cases[-1]
    return answer
