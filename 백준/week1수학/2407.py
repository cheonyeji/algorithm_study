# 2022-10-09
# week1 - 수학. 조합
# https://www.acmicpc.net/problem/2407
# 소요시간 : 12:37~ 13:21 (50m)


n, m = map(int, input().split())


def recur_f(n):
    if n == 1:
        return 1
    else:
        return n * recur_f(n - 1)


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# '/'로 연산해준뒤 int형변환했더니 에러남
# int형으로 나눗셈 결과를 리턴해주는 '//' 사용해서 통과
print(factorial(n) // ((factorial(m) * factorial(n - m))))
