# 2022-07-17
# 프로그래머스 Lv2 - 짝지어 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# 소요시간 : 19:07 ~


def solution(s):
    answer = -1

    leng = len(s)

    while True:
        # 모두 다 제거된 경우
        if s == "":
            return 1

        # 한글자만 남은 경우
        if len(s) < 2:
            break

        # a~z
        for i in range(97, 123):
            s = s.replace(chr(i) * 2, "")

        # 한번도 안 바뀐 경우
        if leng == len(s):
            break

    if len(s) != 0:
        answer = 0
    else:
        answer = 1

    return answer
