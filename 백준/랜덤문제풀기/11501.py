# 2023-09-28 (소요시간 : 30m+풀이참고)
# 문제집 https://www.acmicpc.net/workbook/view/8708
# 실버2. https://www.acmicpc.net/problem/11501

"""
시간초과 접근방법
최대이익이 발생하려면 max값 기준으로 그 앞까지 모든 주식을 구입하고 그날 다 팔아야함
주식 배열을 돌면서 max값을 뽑아내서 계속 부분배열로 처리
더이상 처리해줄 수 없는 길이가 되면 stop

옮은 접근방법
어차피 최대 수익이 나려면 뒤에서부터 계산을 해야함
가장 마지막 날짜가 최대 수익이라고 생각하고, 앞으로 쭉 훑으면서
최대수익보다 현재 금액이 더 크면 갱신 (아무것도 하지 않음)
아니면 수익 계산해주기

배열을 뒤에서부터 살펴보는것도 생각해볼것
"""

from sys import stdin

input = stdin.readline

T = int(input())


def solution():
    N = int(input())
    data = list(map(int, input().split(" ")))

    result = 0
    max_data = data[-1]

    for i in range(len(data) - 2, -1, -1):
        if data[i] > max_data:
            max_data = data[i]
            continue
        result += max_data - data[i]
    return result


answer = []
for _ in range(T):
    answer.append(solution())

for v in answer:
    print(v)
