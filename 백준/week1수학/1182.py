# 2022-10-08
# week1 - 수학. 부분수열의 합
# https://www.acmicpc.net/problem/1182
# 소요시간 : 00:30~ 00:34 (5m)

from itertools import combinations


n, s = map(int, input().split())
data = list(map(int, input().split()))

cnt = 0

for i in range(1, n + 1):
    for j in combinations(data, i):
        if sum(j) == s:
            cnt += 1

print(cnt)
