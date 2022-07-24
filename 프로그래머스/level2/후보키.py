# 2022-07-24
# 프로그래머스 Lv2 - 후보키
# https://school.programmers.co.kr/learn/courses/30/lessons/42890
# 소요 시간 : 16:35 ~ 17:25 (50m)

from itertools import combinations


def solution(relation):
    answer = 0

    column_list = [i for i in range(len(relation[0]))]

    # 모든 후보키가 될 수 있는 경우의 수(컬럼 인덱스 배열)
    cases = []
    for i in range(1, len(column_list) + 1):
        cases.append(list(combinations(column_list, i)))

    ck_list = []
    for case_list in cases:
        for case in case_list:
            all_senario = []
            for row in range(len(relation)):
                arr = [relation[row][c] for c in case]
                all_senario.append(tuple(arr))
            # print(all_senario)

            if len(all_senario) == len(list(set(all_senario))):
                ck_list.append(case)

    # print(ck_list)

    ck = []
    for key in ck_list:
        if len(ck) == 0:
            ck.append(key)
            continue
        cnt = 0
        for k in ck:
            if set(key) != set(k) | set(key):
                cnt += 1

        if cnt == len(ck):
            ck.append(key)

    answer = len(ck)
    return answer
