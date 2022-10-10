# 2022-10-10
# week2 - 자료구조. 제로
# https://www.acmicpc.net/problem/10773
# 소요시간 : 00:20 ~ 00:21 (1m)

import sys

input = sys.stdin.readline

k = int(input())

nums = []
for _ in range(k):
    data = int(input())
    if data != 0:
        nums.append(data)
    else:
        nums.pop()

print(sum(nums))
