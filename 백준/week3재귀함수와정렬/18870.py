# 2022-10-18
# week3 - 재귀함수와 정렬. 좌표 압축
# https://www.acmicpc.net/problem/18870
# 소요시간 : 10:10 ~ 11:07 (60m, 아이디어는 떠올렸으나 마지막부분 해설참고)

import sys

input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split(" ")))

sorted_data = sorted((set(data)))

dictionary = {sorted_data[i]: i for i in range(len(sorted_data))}

answer = ""
for d in data:
    answer += str(dictionary[d]) + " "

print(answer[:-1])
