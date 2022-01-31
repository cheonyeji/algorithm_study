# 2021-01-31
# 이코테 ch11 그리디 문제 Q2 곱하기 혹은 더하기

str = input()

result = int(str[0])

for i in range(1, len(str)):
    if result <= 1 or int(str[i]) <= 1:
        result += int(str[i])
    else:
        result *= int(str[i])

print(result)

"""
TC 1 -> 576
02984
TC 2 -> 210
567
TC 3 -> 576
20984
"""
