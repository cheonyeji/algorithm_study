# 2022-01-15
# 이코테 ch14 정렬 문제 Q26 카드 정렬하기
# https://www.acmicpc.net/problem/1715

import heapq

n = int(input())

# 항상 가장 작은 크기의 두 카드 묶음을 합쳐야 함 ㅠㅠ

q = []

for _ in range(n):
    data = int(input())
    heapq.heappush(q, data)

result = 0

while len(q) != 1:
    # 가장 작은 2개 원소 꺼내기
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    sum_value = a + b
    result += sum_value
    heapq.heappush(q, sum_value)

print(result)

"""
TC 1 -> 100
3
10
20
40
TC 2 -> 410
4
30
40
50
100
TC 3 -> 360
4
30
40
50
60
"""
