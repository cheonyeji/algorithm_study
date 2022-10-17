# 2022-10-17
# week3 - 재귀함수와 정렬. 수 정렬하기 3
# https://www.acmicpc.net/problem/10989
# 소요시간 : 16:32 ~ 16:40 (8m)

"""
메모리가 8MB로 제한되어 있어 sort()함수 사용시 메모리 초과
계수정렬 사용
"""

import sys

input = sys.stdin.readline

N = int(input())

count = [0] * 10001

for _ in range(N):
    num = int(input())
    count[num] += 1

for i in range(len(count)):
    if count[i] == 0:
        continue
    else:
        for _ in range(count[i]):
            print(i)
