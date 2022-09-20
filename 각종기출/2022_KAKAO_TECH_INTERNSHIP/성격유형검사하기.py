# 2022-09-20
# 2022 카카오 테크 인턴십 기출 - 성격유형 검사하기 (프로그래머스 lv1)
# https://school.programmers.co.kr/learn/courses/30/lessons/118666
# 소요 시간 : 11:29~12:04 (35m)


def solution(survey, choices):
    answer = ""

    score = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    # 점수 부여
    for i in range(len(choices)):
        # 동의
        if choices[i] // 4 >= 1:
            score[survey[i][1]] += choices[i] % 4
        # 비동의
        else:
            score[survey[i][0]] += 4 - choices[i]

    # 지표별 유형 판단
    if score["R"] >= score["T"]:
        answer += "R"
    else:
        answer += "T"

    if score["C"] >= score["F"]:
        answer += "C"
    else:
        answer += "F"

    if score["J"] >= score["M"]:
        answer += "J"
    else:
        answer += "M"

    if score["A"] >= score["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer
