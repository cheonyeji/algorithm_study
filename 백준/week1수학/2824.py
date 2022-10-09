# 2022-10-09
# week1 - 수학. 최대공약수
# https://www.acmicpc.net/problem/2824
# 소요시간 : 13:32~ 13:43 (10m)

n = int(input())
numA = map(int, input().split())

a = 1
for num in numA:
    a *= num

m = int(input())
numB = map(int, input().split())

b = 1
for num in numB:
    b *= num


def gcd(a, b):
    while b:
        a, b = b, (a % b)
    return a


result = str(gcd(a, b))

if len(result) > 9:
    print(result[len(result) - 9 :])
else:
    print(result)
