# 2022-06-30
# 프로그래머스 lv1 - 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576
# 소요 시간 : 15:24 ~ 16:19 (55m)

from collections import Counter

# 두 Counter 객체를 빼줘도 Ok (엄청 간결한 코드 )


def solution(participant, completion):
    answer = ""

    c_p = Counter(participant)
    c_c = Counter(completion)

    for key_cp, value_cp in c_p.items():
        # 만약 key가 존재하고 value값이 다르면 answer에 추가
        if key_cp in c_c and value_cp != c_c.get(key_cp):
            answer += key_cp
            break
        # key가 없으면 answer에 추가
        elif not key_cp in c_c:
            answer += key_cp
            break

    return answer
