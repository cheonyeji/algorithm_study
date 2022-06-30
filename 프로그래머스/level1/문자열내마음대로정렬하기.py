## 2022-06-30
# 프로그래머스 lv1 - 문자열 내 마음대로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/12915
# 소요시간 : 1:15 ~ 1:20 (5m)


def solution(strings, n):
    answer = []

    # 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다.
    # lambda 쓰면 아주 쉬운 문제였음. 만약 같은 문자의 경우 사전순 정렬이라 (x[n], x) 로 람다식 추가
    answer = sorted(strings, key=lambda x: (x[n], x))
    return answer
