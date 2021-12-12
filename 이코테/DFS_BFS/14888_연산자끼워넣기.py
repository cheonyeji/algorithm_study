import sys

input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))

operators = list(map(int, input().split()))  # +, -, *, // 순서

max_num = -1e9
min_num = 1e9


def calcul(num, i, plus, minus, mul, div):
    global n, max_num, min_num
    if i == n:
        min_num = min(num, min_num)
        max_num = max(num, max_num)
        return
    else:
        if plus:
            calcul(num + numbers[i], i + 1, plus - 1, minus, mul, div)
        if minus:
            calcul(num - numbers[i], i + 1, plus, minus - 1, mul, div)
        if mul:
            calcul(num * numbers[i], i + 1, plus, minus, mul - 1, div)
        if div:
            if num < 0:
                calcul(-((-num) // numbers[i]), i + 1, plus, minus, mul, div - 1)
            else:
                calcul(num // numbers[i], i + 1, plus, minus, mul, div - 1)


calcul(numbers[0], 1, operators[0], operators[1], operators[2], operators[3])


print(max_num)
print(min_num)

# 순열로 하면 시간초과날라나?
