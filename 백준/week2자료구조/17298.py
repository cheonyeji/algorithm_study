# 2022-10-16, 10-17
# week2 - 자료구조. 오큰수
# https://www.acmicpc.net/problem/17298
# 소요시간 : 22:00 ~ 22:48 (40m, 시간초과), 10:05 ~ 10:38 (33m, 솔)

"""
유효한 비교 대상만 stack에 넣어두면서 살펴봐야 하는 숫자를 최소화하기
"""


import sys

input = sys.stdin.readline

N = int(input())
listA = list(map(int, input().split(" ")))

prev = listA.pop()
answer = [-1]
popped = [prev]


for i in range(len(listA)):
    now = listA.pop()

    if now > prev:
        while len(popped) > 0:
            popped_num = popped.pop()
            if popped_num > now:
                answer.append(popped_num)
                popped.append(popped_num)
                popped.append(now)
                break
        # 무조건 오큰수가 현재 수가 됨
        if len(popped) == 0:
            popped = [now]
            answer.append(-1)

    elif now == prev:
        answer.append(answer[-1])
        popped.append(now)
    else:
        answer.append(prev)
        popped.append(now)

    prev = now


print(" ".join(map(str, answer[::-1])))
