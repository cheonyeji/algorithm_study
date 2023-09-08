# 2023-07-11
# 백준 - 다익스트라
# https://www.acmicpc.net/problem/1446
# 소요 시간 : 1h 30m

"""
다익스트라 문제이나 dp처럼 예전 상태에 의존해서 풀어도 되는 문제 (heapq 사용X)
노드가 따로 존재하지 않고 모든 좌표의 데이터를 살펴보아야 하나, 최대 노드 길이가 10000으로 고정되어 OK
"""

from sys import stdin

input = stdin.readline

N, D = map(int, input().split())

d = [i for i in range(D + 2)]  # 최단거리 테이블

data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

for i in range(1, D + 1):
    d[i] = min(d[i], d[i - 1] + 1)

    for item in data:
        start, end, dist = item
        if end == i:
            d[end] = min(d[start] + dist, d[end])

print(d[D])
