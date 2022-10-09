# 2022-10-09
# week1 - 수학. 모든 순열
# https://www.acmicpc.net/problem/10947
# 소요시간 : 13:29~ : (m)

from itertools import permutations


n = int(input())

result = list(permutations(range(1, n + 1)))

for i in result:
    print(" ".join(map(str, i)))
