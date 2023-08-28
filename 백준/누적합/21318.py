# 2023-08-28 (소요시간 : x 해설참고)
# 누적합 https://www.acmicpc.net/problem/21318

"""
실수를 몇번했는지 누적합으로 계산해서 구간 내의 실수를 출력해주면 됨
"""

from sys import stdin

input = stdin.readline

N = int(input())

data = list(map(int, input().split(" ")))

mistake = [0 for _ in range(N)]  # i번째 값 = i번째 곡까지 몇번 실수했는가

for i in range(N):
    if i == 0:
        continue
    if data[i] < data[i - 1]:
        mistake[i] = mistake[i - 1] + 1
    else:
        mistake[i] = mistake[i - 1]

Q = int(input())

for _ in range(Q):
    s, e = map(int, input().split(" "))
    print(mistake[e - 1] - mistake[s - 1])
