# 2022-10-17
# week3 - 재귀함수와 정렬. 소트인사이드
# https://www.acmicpc.net/problem/1427
# 소요시간 : 16:53 ~ 16:56 (3m)


import sys

input = sys.stdin.readline

num = list(input().replace("\n", ""))
num.sort(reverse=True)

print("".join(num))
