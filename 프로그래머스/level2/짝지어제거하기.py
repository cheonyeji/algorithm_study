# 2022-07-17
# 프로그래머스 Lv2 - 짝지어 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# 소요시간 : 19:07 ~


def solution(s):
    answer = -1
    stack = []

    for c in s:
        if len(stack) != 0 and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    if len(stack) != 0:
        return 0
    else:
        return 1

    return answer
