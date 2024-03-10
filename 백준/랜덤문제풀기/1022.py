# 2023-09-30
# 백준 소용돌이 예쁘게 출력하기 https://www.acmicpc.net/problem/1022
from sys import stdin
from collections import defaultdict

input = stdin.readline

# 정사각형 가로or세로 넓이

r1, c1, r2, c2 = map(int, input().split(" "))

size = max(abs(r1), abs(r2), abs(c1), abs(c2)) * 2 + 1

num = 1

# 시작좌표
sr, sc = 0, 0
r, c = sr, sc

# 상 좌 하 우 (반시계)
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


pos = defaultdict(int)
if r1 <= 0 <= r2 and c1 <= 0 <= c2:
    pos[(0, 0)] = 1

cnt = 1
while cnt < size:
    # 우로 1번
    num += 1
    r += dr[3]
    c += dc[3]
    if r1 <= r <= r2 and c1 <= c <= c2:
        pos[(r, c)] = num
    # 위로 cnt번
    for _ in range(cnt):
        num += 1
        r += dr[0]
        c += dc[0]
        if r1 <= r <= r2 and c1 <= c <= c2:
            pos[(r, c)] = num
    cnt += 1
    # 좌 하 우 cnt번
    for i in range(1, 4):
        for _ in range(cnt):
            num += 1
            r += dr[i]
            c += dc[i]
            if r1 <= r <= r2 and c1 <= c <= c2:
                pos[(r, c)] = num
    cnt += 1

# 가장 큰 수 기준 공백 삽입
leng = len(str(num))

# 자릿수 맞추기
for r in range(r1, r2 + 1):
    for c in range(c1, c2 + 1):
        n = pos[(r, c)]
        print(" " * (leng - len(str(n))) + str(n), end=" ")
    print()


###################################### 초기 풀이(시초)
# pos = []
# nums = []
# if r1 <= 0 <= r2 and c1 <= 0 <= c2:
#     pos.append((0, 0))
#     nums.append(1)

# cnt = 1
# while cnt < size:
#     # 우로 1번
#     num += 1
#     r += dr[3]
#     c += dc[3]
#     # check를 직접 보지 말것...............
#     if r1 <= r <= r2 and c1 <= c <= c2:
#         pos.append((r, c))
#         nums.append(num)
#     # 위로 cnt번
#     for _ in range(cnt):
#         num += 1
#         r += dr[0]
#         c += dc[0]
#         if r1 <= r <= r2 and c1 <= c <= c2:
#             pos.append((r, c))
#             nums.append(num)
#     cnt += 1
#     # 좌 하 우 cnt번
#     for i in range(1, 4):
#         for _ in range(cnt):
#             num += 1
#             r += dr[i]
#             c += dc[i]
#             if r1<= r <= r2 and c1 <= c <= c2 :
#                 pos.append((r, c))
#                 nums.append(num)
#     cnt += 1

# # 가장 큰 수 기준 공백 삽입
# leng = len(str(num))

# # 자릿수 맞추기
# for r in range(r1, r2+ 1):
#     for c in range(c1, c2+ 1):
#         n = nums[pos.index((r, c))]
#         print(" " * (leng - len(str(n))) + str(n), end=" ")
#     print()
