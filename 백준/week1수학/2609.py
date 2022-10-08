# 2022-10-08
# week1 - 수학. 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609
# 소요시간 : 15:30 ~ 15:50 (20m)

n, m = map(int, input().split())

# 가장 베이직한 방법
def getGCD_basic(x, y):
    for i in range(min(x, y), 0, -1):
        if x % i == 0 and y % i == 0:
            return i


def getLCM_basic(x, y):
    for i in range(max(x, y), (x * y) + 1):
        if i % x == 0 and i % y == 0:
            return i


# 유클리드 호제법
def getGCD_euclid(x, y):
    while y:
        x, y = y, x % y
    return x


def getLCM_euclid(x, y):
    return (x * y) // getGCD_euclid(x, y)


# 파이썬 라이브러리 활용
import math

print(math.gcd(n, m))
print(math.lcm(n, m))
