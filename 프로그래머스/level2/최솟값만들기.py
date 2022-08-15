# 2022-08-15
# 프로그래머스 Lv2 - 최솟값 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12941
# 소요 시간 : 16:15 ~ 16:30 (15m)


def solution(A, B):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer
