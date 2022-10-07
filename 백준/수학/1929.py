# 2022-10-07
# week1. 수학
# https://www.acmicpc.net/problem/1929
# 소요시간 : 18:07 ~ 18:12 (5m)

import math

# 제곱근까지만 보면 OK
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


m, n = map(int, input().split())

for num in range(m, n + 1):
    if num == 1:
        continue
    if isPrime(num):
        print(num)
