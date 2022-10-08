# 2022-10-07
# week1. 수학
# https://www.acmicpc.net/problem/1978
# 소요시간 : 18:22 ~ 18:24 (2m)

import math

# 제곱근까지만 보면 OK
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
data = list(map(int, input().split()))

cnt = 0
for num in data:
    if isPrime(num):
        cnt += 1

print(cnt)
