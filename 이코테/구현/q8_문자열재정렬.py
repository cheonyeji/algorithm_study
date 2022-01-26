# 2021-01-26
# 이코테 ch12 구현 문제 Q8 문자열 재정렬

str = input()

result = []
num = 0
for i in str:
    if 65 <= ord(i) <= 90:
        result.append(i)
    else:
        num += int(i)


result.sort()

for i in result:
    print(i, end="")
print(num)

"""
TC 1 -> ABCKK13
K1KA5CB7
TC 2 -> ADDIJJJKKLSS20
AJKDLSI412K4JSJ9D
"""
