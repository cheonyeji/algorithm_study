# 2023-08-28 (소요시간 : 30m 넘어가도 시간단축 생각 안나서 해설)
# 누적합 https://www.acmicpc.net/problem/1806

"""
완탐으로 풀면 O(N^2)라서 시간초과
투 포인터로 접근해서 풀어야 한다
누적 값이 S보다 크면 개수를 체크하고 왼쪽 포인터를 1 증가
S보다 작으면 오른쪽 포인터를 1 증가
"""
from sys import stdin

input = stdin.readline

N, S = map(int, input().split())
data = list(map(int, input().split()))

start, end = 0, 0
sum_ = data[0]
answer = 100001

while True:
    if sum_ >= S:
        sum_ -= data[start]
        answer = min(answer, end - start + 1)
        start += 1
    else:
        end += 1
        if end == N:
            break
        sum_ += data[end]

if answer == 100001:
    print(0)
else:
    print(answer)
