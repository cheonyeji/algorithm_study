# 2022-10-17
# week3 - 재귀함수와 정렬. 나무 조각
# https://www.acmicpc.net/problem/2947
# 소요시간 : 16:57 ~ 17:01 (4m)

import sys

input = sys.stdin.readline


num = list(map(int, input().split(" ")))

sorted_num = sorted(num)

while True:

    if sorted_num == num:
        break

    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            num[i], num[i + 1] = num[i + 1], num[i]
            print(" ".join(map(str, num)))
