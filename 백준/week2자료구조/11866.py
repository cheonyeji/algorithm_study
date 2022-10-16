# 2022-10-16
# week2 - 자료구조. 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866
# 소요시간 : 20:25 ~ 20:54 (30m)

"""
원형 큐를 구현해야 된다고 생각했는데 쉽게 가도 됬다.
k번째 수가 나오기 전까지는 popleft()해준뒤 다시 append()해주고
k번째 수면 popleft()하여 배열에 따로 저장한다.
해당 배열을 문제에서 원하는 형식으로 출력해주면 된다.
"""

from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split(" "))

q = deque()

for i in range(1, N + 1):
    q.append(i)

yosep = []
while len(q) > 0:
    for _ in range(K - 1):
        data = q.popleft()
        q.append(data)
    yosep.append(q.popleft())

print("<" + ", ".join(map(str, yosep)) + ">")
