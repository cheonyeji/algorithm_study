# 곱집합 구하기
import itertools

str1 = "ABCD"
str2 = "xy"
str3 = "1234"

print(list(itertools.product(str1, str2, str3)))
