# 2022-10-08
# week1 - 수학. 소인수분해
# https://www.acmicpc.net/problem/11653
# 소요시간 : 22:28 ~ 22:41 (15m)

n = int(input())

for i in range(2, n + 1):
    if n == 1:
        break
    while n % i == 0:
        n /= i
        print(i)
