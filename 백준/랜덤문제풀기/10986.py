# 2023-10-01
# 백준 나머지 합 https://www.acmicpc.net/problem/10986

from sys import stdin
from itertools import combinations

input = stdin.readline

N, M = map(int, input().split(" "))
data = list(map(int, input().split(" ")))

mod = [i % M for i in data]

answer = 0

# 시간초과
# idx = [i for i in range(N)]

# for n1, n2 in combinations_with_replacement(idx, 2):
#     if (acc[n2] - acc[n1 - 1]) % M == 0:
#         answer += 1

# print(answer)

# 시간초과 (n^2라서...)
# answer = 0
# part_acc = 0
# for i in range(N):
#     for j in range(i, N):
#         part_acc = acc[j] - acc[i - 1]
#         if part_acc % M == 0:
#             answer += 1
# print(answer)
