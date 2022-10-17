# 2022-10-17
# week3 - 재귀함수와 정렬. 피보나치 수 5
# https://www.acmicpc.net/problem/10870
# 소요시간 : 15:10 ~ 15:15 (5m)


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibo(n - 1) + fibo(n - 2)


N = int(input())
print(fibo(N))
