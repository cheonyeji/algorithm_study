# 2022-10-16
# week2 - 자료구조. 회전하는 큐
# https://www.acmicpc.net/problem/1021
# 소요시간 : 12:16 ~ 12:57 (40m)


"""
큐 안의 숫자는 중복이 없고 뽑아낼 타켓은 그 안에 무조건 존재하므로 
index 기능을 사용하여 해당 숫자(타켓)의 위치를 알아낸다.
만약 해당 숫자가 큐의 중간보다 뒤에 있으면 오른쪽 이동을,
중간과 같거나 그보다 앞에 있으면 왼쪽 이동을 해주면 됨
"""


import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split(" "))
data = list(map(int, input().split(" ")))

q = deque()

for i in range(1, N + 1):
    q.append(i)

answer = 0
for num in data:
    op2, op3 = 0, 0
    idx = q.index(num)
    if idx > len(q) // 2:
        op3 = len(q) - idx
        for i in range(op3):
            q.appendleft(q.pop())
        answer += op3
    else:
        op2 = idx
        for i in range(op2):
            q.append(q.popleft())
        answer += op2
    q.popleft()

print(answer)
