# 2021-01-30
# 이코테 ch12 구현 문제 Q13 치킨 배달
# https://www.acmicpc.net/problem/15686

from itertools import combinations


INF = int(1e9)
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []

for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            house.append([r, c])
        if graph[r][c] == 2:
            chicken.append([r, c])

# 폐업시키지 않을 치킨 집을 최대 m개 골랐을 때, 도시의 치킨 거리의 최솟값 출력
# 치킨 거리 = 집 <-> 치킨 중 가장 가까운 거리
# 도시의 치킨 거리 = 모든 치킨 거리의 합

# 치킨 거리 계산
def calcul_chicken_dist(hx, hy, new_chicken):
    min_dist = INF
    for i in new_chicken:
        d = abs(hx - i[0]) + abs(hy - i[1])
        if min_dist > d:
            min_dist = d

    return min_dist


# m개의 치킨집만 뽑는 경우의 수 계산
cases = list(combinations(chicken, m))

city_chicken_dist = INF
for case in cases:
    sum_dist = 0
    for h in house:
        sum_dist += calcul_chicken_dist(h[0], h[1], case)

    if city_chicken_dist > sum_dist:
        city_chicken_dist = sum_dist

print(city_chicken_dist)

"""
TC 1 -> 5
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
"""
