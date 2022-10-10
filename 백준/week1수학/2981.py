# 2022-10-10
# week1 - 수학. 검문
# https://www.acmicpc.net/problem/2981
# 소요시간 : 20:20 ~ 21:40 (60m, 풀이참고)

import math
import sys

input = sys.stdin.readline

n = int(input())

nums = sorted([int(input()) for _ in range(n)])

gaps = []
for i in range(1, len(nums)):
    gaps.append(abs(nums[i] - nums[i - 1]))

answer = math.gcd(*gaps)

answer_list = []
i = 2

# 약수 구하는 while문 (통과)
while i <= (answer ** (1 / 2)) + 1:
    if answer % i == 0:
        answer_list.append(i)
        if i != (answer // i):
            answer_list.append(answer // i)
    i += 1

# 약수 구하는 for문 (시간초과)
# for i in range(2, int(answer ** 1/2)+1):
#     if answer % i == 0:
#         answer_list.append(i)
#         if i != (answer // i):
#             answer_list.append(answer//i)

for i in sorted(list(set(answer_list))):
    print(i, end=" ")

print(answer)
