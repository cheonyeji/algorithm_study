# 2022-10-10
# week1 - 수학. 숨바꼭질 6
# https://www.acmicpc.net/problem/17087
# 소요시간 : 14:25~ 14:47 (20m)

import math


n, s = map(int, input().split())

data = list(map(int, input().split()))

gaps = []

for v in data:
    gaps.append(abs(s - v))


print(math.gcd(*gaps))
