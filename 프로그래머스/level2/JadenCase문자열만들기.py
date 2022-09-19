# 2022-09-19
# 프로그래머스 lv2 - JadenCase 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12951
# 소요 시간 : 11:39~12:00, 13:05~13:49 (65m)

"""
문자열의 길이가 최대 200이기 때문에 하나하나 보면서 처리

1. 가장 처음 등장하는 경우
2. 공백 문자가 여러번 등장하는 경우

이렇게 2가지 케이스를 고려해준 뒤, 만약 앞의 글자가 공백이라면 (=단어시작) upper로 변환
숫자가 나와도 upper 함수는 소문자->대문자 변환만 해주기 때문에 상관 X

"""


def solution(s):
    answer = ""

    for i in range(len(s)):
        if i == 0:
            if 48 <= ord(s[i]) <= 57:
                answer += s[i]
            else:
                answer += s[i].upper()
            continue

        if s[i] == " ":
            answer += s[i]
            continue

        if s[i - 1] == " ":
            answer += s[i].upper()
        else:
            answer += s[i].lower()

    return answer
